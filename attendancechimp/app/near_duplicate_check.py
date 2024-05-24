import cv2
import numpy as np
from image_similarity_measures.quality_metrics import ssim
from .models import QRCodeUpload, RedFlag
from django.core.files.base import ContentFile
from PIL import Image

def check_near_duplicates():
    uploads = QRCodeUpload.objects.all()
    images = []

    for upload in uploads:
        # Load image using PIL
        image_pil = Image.open(upload.image)
        image_rgba = image_pil.convert("RGB")
        # Resize image
        image_resized = image_rgba.resize((350, 350))
        # Convert PIL image to numpy array
        image_np = np.array(image_resized)
        images.append((upload, image_np))

    for i in range(len(images)):
        for j in range(i + 1, len(images)):
            upload1, img1 = images[i]
            upload2, img2 = images[j]
            similarity = ssim(img1, img2)
            if similarity > 0.95:  # arbitrary threshold for near-duplicate detection
                flag_image(upload1, "Near duplicate detected")
                flag_image(upload2, "Near duplicate detected")

def flag_image(upload, reason):
    upload.image.seek(0)
    flagged_image = ContentFile(upload.image.read())
    RedFlag.objects.create(student=upload.student, image=flagged_image, reason=reason)
