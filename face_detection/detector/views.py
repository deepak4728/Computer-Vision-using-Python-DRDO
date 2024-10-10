from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import ImageUploadForm
from .models import UploadedImage
import cv2
import os
from urllib.parse import urlencode


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save()
            img_path = img.image.path
            detected_faces_path, num_faces = detect_faces(img_path)
            query_string = urlencode({'detected_faces_path': detected_faces_path, 'num_faces': num_faces})
            url = f"{request.build_absolute_uri('result/')}?{query_string}"
            return HttpResponseRedirect(url)
    else:
        form = ImageUploadForm()
    return render(request, 'face_upload.html', {'form': form})

def detect_faces(img_path):
    img = cv2.imread(img_path)
    if img is None:
        raise ValueError(f"Image not found or unable to load: {img_path}")
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Adjust these parameters for better detection
    scaleFactor = 1.05
    minNeighbors = 9
    
    faces = face_cascade.detectMultiScale(gray, scaleFactor, minNeighbors)
    
    # Debug: print detected faces coordinates
    print(f"Detected faces: {faces}")
    
    num_faces = len(faces)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    detected_faces_dir = os.path.join('media', 'detected_faces')
    if not os.path.exists(detected_faces_dir):
        os.makedirs(detected_faces_dir)
    
    detected_faces_path = os.path.join(detected_faces_dir, 'detected_' + os.path.basename(img_path))
    cv2.imwrite(detected_faces_path, img)
    
    return detected_faces_path, num_faces

def result(request):
    detected_faces_path = request.GET.get('detected_faces_path')
    num_faces = request.GET.get('num_faces')
    return render(request, 'face_result.html', {'detected_faces_path': detected_faces_path, 'num_faces': num_faces})