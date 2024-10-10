
# Create your views here.
import cv2
import base64
import numpy as np
from django.shortcuts import render
from .forms import UploadImageForm

def edge_detection_view(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image_array = np.fromstring(image.read(), np.uint8)
            img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)

            # Perform edge detection
            edges = cv2.Canny(img, 100, 200)

            # Encode the image back to a format suitable for displaying in HTML
            _, buffer = cv2.imencode('.jpg', edges)
            edges_encoded = buffer.tobytes()
            encoded_image = base64.b64encode(edges_encoded).decode('utf-8')

            return render(request, 'edge_result.html', {'image': encoded_image})
    else:
        form = UploadImageForm()

    return render(request, 'edge_upload.html', {'form': form})
