from django.shortcuts import render

# Create your views here.
# classifier/views.py

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
from .inception_model import classify_image

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            file_path = fs.save(image.name, image)
            file_url = fs.url(file_path)

            # Classify the image
            predictions = classify_image(fs.path(file_path))

            return render(request, 'classifier_result.html', {'file_url': file_url, 'predictions': predictions})
    else:
        form = ImageUploadForm()
    return render(request, 'classifier_upload.html', {'form': form})
