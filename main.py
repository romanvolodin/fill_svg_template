import argparse
import csv
from os import system
from pathlib import Path

from environs import Env


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Скрипт для рендера SVG-шаблонов в PDF (и не только)",
    )
    parser.add_argument(
        "-t",
        "--template",
        type=str,
        help="Путь к SVG-шаблону",
        required=True,
    )
    parser.add_argument(
        "-d",
        "--data",
        type=str,
        help="Путь к данным для вставки в шаблон",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="output",
        help=("Путь к директории, куда сохранять результаты. По умолчанию: ./output"),
    )
    return parser.parse_args()


def fill_svg(template_path, output_path, context):
    with open(template_path, encoding="utf8") as input_svg:
        content = input_svg.read()

    formatted_content = content.format(**context)

    with open(output_path, "w", encoding="utf8") as output_svg:
        return output_svg.write(formatted_content)


if __name__ == "__main__":
    env = Env()
    env.read_env()
    inkscape = env.str("INKSCAPE")

    args = parse_arguments()
    template_path = Path(args.template)
    template_name = template_path.stem

    output_dir = Path(args.output)
    output_dir.mkdir(exist_ok=True)

    with open(args.data) as csv_file:
        reader = csv.DictReader(csv_file, delimiter="\t")

        for row in reader:
            output_svg_path = output_dir / f"{template_name}_{row['title']}_filled.svg"
            output_path = output_dir / f"{template_name}_{row['title']}.pdf"

            fill_svg(
                template_path,
                output_svg_path,
                row,
            )

            system(
                f"{inkscape} --export-type=pdf "
                f"--export-filename='{output_path}' '{output_svg_path}'"
            )

            output_svg_path.unlink()
