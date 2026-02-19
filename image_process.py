import cv2
import uuid
import os

def to_greyscale(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Could not read the image")

    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    os.makedirs("media/output", exist_ok=True)

    filename = f"{uuid.uuid4()}.png"
    output_path = os.path.join("media", "output", filename)

    success = cv2.imwrite(output_path, grayimg)
    if not success:
        raise RuntimeError("Failed to write image")

    return output_path


def to_blur_gaussian(image_path , ksize=21):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Could not read the image")
    
    filename = f"{uuid.uuid4()}.png"
    
    output_path = os.path.join("media","output",filename)
    
    blurred_img = cv2.GaussianBlur(img , (ksize,ksize), 0)

    success = cv2.imwrite(output_path, blurred_img)

    if not success:
        raise RuntimeError("Failed to write image")
    
    return output_path