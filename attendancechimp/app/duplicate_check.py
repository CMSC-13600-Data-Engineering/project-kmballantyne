from .models import QRCodeUpload, RedFlag
from django.core.files.base import ContentFile

def check_duplicates():
    uploads = QRCodeUpload.objects.all()
    unique_images = {}

    for upload in uploads:
        image_content = upload.image.read()
        if image_content in unique_images:
            # If duplicate, flag both images
            original_upload = unique_images[image_content]
            flag_image(original_upload, "Exact duplicate detected")
            flag_image(upload, "Exact duplicate detected")
        else:
            unique_images[image_content] = upload

def flag_image(upload, reason):
    # Save image to RedFlag table
    flagged_image = ContentFile(upload.image.read())
    RedFlag.objects.create(student=upload.student, image=flagged_image, reason=reason)
