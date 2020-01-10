import argparse

from pathlib import Path
from PIL import Image
from resizeimage import resizeimage

DATASETS = {
    "montgomery": "Montgomery/MontgomerySet/CXR_png/",
    "china": "ChinaSet_AllFiles/ChinaSet_AllFiles/CXR_png/",
}
FINAL_IMAGE_SIZE = [512, 512]


def process_dataset(input_path, output_path):
    if not output_path.exists():
        output_path.mkdir(parents=True)

    for image in input_path.glob("*.png"):
        with image.open("rb") as fd_img:
            img = Image.open(fd_img)
            img = resizeimage.resize_cover(img, FINAL_IMAGE_SIZE)
            img.save(output_path.joinpath(image.name), img.format)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Crops and resizes images")
    parser.add_argument(
        "-d",
        "--dataset-dir",
        dest="dataset_dir",
        required=True,
        help="Path to the kaggle dataset directory",
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        dest="output_dir",
        help="Destination for the cropped images",
        default="output",
    )
    args = parser.parse_args()

    dataset_path = Path(args.dataset_dir)
    output_path = Path(args.output_dir)

    for dataset in DATASETS:
        process_dataset(dataset_path / DATASETS[dataset], output_path / dataset)
