import argparse
import hashlib
import json
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageOps


USER_AGENT = "FruitAnimalClassifierBootcamp/1.0"
BASE_URL = "https://loremflickr.com/360/260/{tags}?lock={lock}"

TAGS = {
    "fruit": [
        "apple,fruit",
        "banana,fruit",
        "orange,fruit",
        "strawberry,fruit",
        "grapes,fruit",
        "pineapple,fruit",
        "kiwi,fruit",
        "mango,fruit",
        "pear,fruit",
        "watermelon,fruit",
        "peach,fruit",
        "lemon,fruit",
    ],
    "animal": [
        "cat,animal",
        "dog,animal",
        "horse,animal",
        "cow,animal",
        "elephant,animal",
        "bird,animal",
        "fox,animal",
        "sheep,animal",
        "rabbit,animal",
        "lion,animal",
        "deer,animal",
        "monkey,animal",
    ],
}

DEMO_TAGS = {
    "fruit": ["kiwi,fruit", "mango,fruit"],
    "animal": ["fox,animal", "sheep,animal"],
}


def download_image(url):
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read(), response.geturl()


def save_normalized(image_bytes, output_path):
    tmp_path = output_path.with_suffix(".download")
    tmp_path.write_bytes(image_bytes)
    try:
        with Image.open(tmp_path) as image:
            image = ImageOps.exif_transpose(image)
            if image.width < 150 or image.height < 150:
                return False
            image = image.convert("RGB")
            image.thumbnail((512, 512))
            image.save(output_path, format="JPEG", quality=90)
            return True
    finally:
        if tmp_path.exists():
            tmp_path.unlink()


def clear_old_images(folder):
    folder.mkdir(parents=True, exist_ok=True)
    for path in folder.glob("*.jpg"):
        path.unlink()


def collect_class(class_name, output_dir, target_count, clean, start_lock):
    output_dir = Path(output_dir)
    if clean:
        clear_old_images(output_dir)
    else:
        output_dir.mkdir(parents=True, exist_ok=True)

    records = []
    seen = set()
    attempts = 0
    image_number = len(list(output_dir.glob("*.jpg"))) + 1
    lock = start_lock

    while image_number <= target_count:
        tag = TAGS[class_name][(image_number - 1) % len(TAGS[class_name])]
        url = BASE_URL.format(tags=tag, lock=lock)
        attempts += 1
        lock += 1

        try:
            image_bytes, final_url = download_image(url)
        except Exception as exc:
            print(f"Skipped {url}: {exc}")
            time.sleep(0.5)
            continue

        digest = hashlib.sha256(image_bytes).hexdigest()
        if digest in seen:
            continue
        seen.add(digest)

        simple_tag = tag.split(",")[0].replace(" ", "_")
        output_path = output_dir / f"{class_name}_{image_number:03d}_{simple_tag}.jpg"
        try:
            if save_normalized(image_bytes, output_path):
                records.append(
                    {
                        "class": class_name,
                        "keyword": tag,
                        "request_url": url,
                        "final_url": final_url,
                        "saved_as": str(output_path),
                    }
                )
                print(f"Saved {output_path}", flush=True)
                image_number += 1
        except Exception as exc:
            print(f"Skipped invalid image from {url}: {exc}")

        if attempts > target_count * 5:
            raise RuntimeError(f"Could not collect enough images for {class_name}")
        time.sleep(0.2)

    return records


def collect_demo_images(output_dir, clean):
    output_dir = Path(output_dir)
    if clean:
        clear_old_images(output_dir)
    else:
        output_dir.mkdir(parents=True, exist_ok=True)

    records = []
    lock = 9000
    for class_name, tags in DEMO_TAGS.items():
        for index, tag in enumerate(tags, start=1):
            output_path = output_dir / f"demo_{class_name}_{index}.jpg"
            url = BASE_URL.format(tags=tag, lock=lock)
            lock += 1
            image_bytes, final_url = download_image(url)
            save_normalized(image_bytes, output_path)
            records.append(
                {
                    "class": class_name,
                    "keyword": tag,
                    "request_url": url,
                    "final_url": final_url,
                    "saved_as": str(output_path),
                }
            )
            print(f"Saved {output_path}", flush=True)
            time.sleep(0.2)
    return records


def write_sources(path, records):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Dataset Sources",
        "",
        "This small classroom dataset was downloaded with keyword queries from LoremFlickr.",
        "The images are intended for a one-day educational exercise. For company or production use, replace them with a reviewed, licensed dataset.",
        "",
        f"- Endpoint pattern: `{BASE_URL}`",
        "- Lesson labels: `animal` and `fruit`.",
        "- The `demo_*` files are not stored in `data/images`, so they are outside the model training folder.",
        "",
        "| Class | Saved file | Keyword | Request URL | Final URL |",
        "|---|---|---|---|---|",
    ]
    for record in records:
        lines.append(
            f"| {record['class']} | `{record['saved_as']}` | `{record['keyword']}` | "
            f"[request]({record['request_url']}) | [image]({record['final_url']}) |"
        )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="data/images")
    parser.add_argument("--demo-dir", default="data/demo_inputs")
    parser.add_argument("--target-per-class", type=int, default=150)
    parser.add_argument("--metadata-path", default="docs/DATASET_SOURCES.md")
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove existing generated jpg files from the output folders first.",
    )
    args = parser.parse_args()

    records = []
    records.extend(
        collect_class(
            "fruit",
            Path(args.output_dir) / "fruit",
            args.target_per_class,
            clean=args.clean,
            start_lock=1000,
        )
    )
    records.extend(
        collect_class(
            "animal",
            Path(args.output_dir) / "animal",
            args.target_per_class,
            clean=args.clean,
            start_lock=5000,
        )
    )
    records.extend(collect_demo_images(args.demo_dir, clean=args.clean))
    write_sources(args.metadata_path, records)

    summary = {
        "fruit_images": len(list((Path(args.output_dir) / "fruit").glob("*.jpg"))),
        "animal_images": len(list((Path(args.output_dir) / "animal").glob("*.jpg"))),
        "demo_images": len(list(Path(args.demo_dir).glob("*.jpg"))),
    }
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == "__main__":
    main()
