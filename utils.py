import os
from pathlib import Path

from PIL import Image


def main():
    source_folder = "./images-dataset"
    target_folder = "./images_jpg"

    os.makedirs(target_folder, exist_ok=True)

    target_size = (224, 224)

    supported_formats = [".jpg", "jpeg", ".png", ".jfif", ".webp", ".avif"]

    for filepath in Path(source_folder).rglob("*"):
        if filepath.suffix.lower() not in supported_formats:
            continue
        try:
            img = Image.open(filepath).convert("RGB")
            img = img.resize(target_size)
            target_path = Path(target_folder) / (filepath.stem + ".jpg")
            img.save(target_path, "JPEG")
        except Exception as e:
            print(f"Failed {filepath.name}: {e}")

    print(f"All images are converted and resized to {target_folder}")


if __name__ == "__main__":
    main()
