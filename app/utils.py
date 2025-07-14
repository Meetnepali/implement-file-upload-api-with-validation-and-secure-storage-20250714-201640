from fastapi import UploadFile, HTTPException, status
from pathlib import Path
from PIL import Image
import os
import shutil

MAX_FILE_SIZE = 2*1024*1024
ALLOWED_TYPES = ["image/png", "image/jpeg"]
USER_MEDIA_ROOT = Path("media")


def save_image(file: UploadFile, user_id: str) -> Path:
    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(status_code=400, detail="Only PNG and JPEG images are allowed.")
    file.file.seek(0, os.SEEK_END)
    size = file.file.tell()
    if size > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="Image exceeds maximum size of 2MB.")
    file.file.seek(0)

    user_path = USER_MEDIA_ROOT / user_id
    user_path.mkdir(parents=True, exist_ok=True)
    image_path = user_path / file.filename
    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return image_path

def generate_thumbnail(image_path: Path):
    try:
        with Image.open(image_path) as img:
            img.thumbnail((128, 128))
            thumbnail_path = image_path.parent / f"thumb_{image_path.name}"
            img.save(thumbnail_path)
    except Exception:
        pass
