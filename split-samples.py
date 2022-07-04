import argparse
import cv2
import sys
from pathlib import Path


def split_sample(path: Path, destination: Path):
    """
    Splits a sample into individual syllabics
    """
    box_path = path.with_suffix(".box")
    if not box_path.exists():
        print("Error: No matching box file for {}.".format(path))

    image = cv2.imread(path.resolve().as_posix())
    height, width, depth = image.shape

    box_lines = box_path.read_bytes().decode('utf-8').splitlines()
    for i, line in enumerate(box_lines, 1):
        if len(line.split(" ")) > 6:
            print("Warn: Invalid line {} on line {}".format(line, i))
            continue

        # Tesseract box format is:
        # <symbol> <left> <bottom> <right> <top> <page>
        symbol, left, bottom, right, top, page = line.split(" ")

        if not symbol:
            print("Warn: Missing symbol on line {}".format(i))
            continue

        x = int(left)
        y = height - int(top)
        h = (height - int(bottom)) - y
        w = int(right) - x

        symbol_path = destination.joinpath("{}_{}.png".format(i, symbol))
        cv2.imwrite(symbol_path.as_posix(), image[y:y+h, x:x+w])


def split_samples(samples_path: Path, destination: Path, force: bool):
    """
    Splits all the samples in a directory into individual images.

    Each sample will be given a folder in the destination directory containing
    images of each syllabic.
    """
    if not samples_path.exists():
        sys.exit("Error: Samples path does not exist. Nothing to do.")

    if not destination.exists():
        destination.mkdir(parents=True)

    image_suffixes = {'.jpg', '.jpeg', '.tiff', '.tif', '.png'}

    for file in samples_path.glob("**/*"):
        if not file.suffix.lower() in image_suffixes:
            continue

        print("Processing {}...".format(file.stem))

        output_path = destination.joinpath(file.stem)
        if not force and output_path.exists():
            print(
                "Warn: Sample {} already exists. Use --force to overwrite.".format(output_path))
            continue

        if force and output_path.exists():
            for f in output_path.glob("**/*"):
                if f.is_file():
                    f.unlink()

        output_path.mkdir(parents=True, exist_ok=True)
        split_sample(file.resolve(), output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser("split-samples")
    parser.add_argument(
        "samples_path", help="Input folder to split samples from.",
        type=str, nargs="?", default="samples")
    parser.add_argument(
        "destination", help="Destination folder for split samples.",
        type=str, nargs="?", default="split-samples")
    parser.add_argument(
        "--force", help="Overwrite samples if already exist.",
        action=argparse.BooleanOptionalAction)

    args = parser.parse_args()
    force = args.force
    samples_path = Path(args.samples_path)
    destination = Path(args.destination)

    split_samples(samples_path, destination, force)
