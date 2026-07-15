from pathlib import Path

import numpy as np
from PIL import Image, ImageOps


IMAGE_SIZE = (96, 96)
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def image_files(folder):
    """Return image paths in a stable order."""
    folder = Path(folder)
    return sorted(
        path
        for path in folder.rglob("*")
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
    )


def load_rgb_image(path, image_size=IMAGE_SIZE):
    """Open an image, fix camera rotation, convert it to RGB, and resize it."""
    image = Image.open(path)
    image = ImageOps.exif_transpose(image)
    image = image.convert("RGB")
    return image.resize(image_size)


def extract_features(path, image_size=IMAGE_SIZE):
    """Turn one picture into numbers the model can learn from."""
    image = load_rgb_image(path, image_size=image_size)
    pixels = np.asarray(image, dtype=np.float32) / 255.0

    color_features = []
    for channel in range(3):
        histogram, _ = np.histogram(
            pixels[:, :, channel], bins=24, range=(0.0, 1.0), density=True
        )
        color_features.extend(histogram)

    average_color = pixels.mean(axis=(0, 1))
    color_spread = pixels.std(axis=(0, 1))
    small_pixels = np.asarray(image.resize((16, 16)), dtype=np.float32).reshape(-1)
    small_pixels = small_pixels / 255.0

    return np.concatenate(
        [np.array(color_features), average_color, color_spread, small_pixels]
    )


def make_feature_matrix(paths):
    return np.vstack([extract_features(path) for path in paths])
