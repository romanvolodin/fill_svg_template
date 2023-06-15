import argparse
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

    output_svg_path = output_dir / f"{template_name}_filled.svg"
    output_path = output_dir / f"{template_name}.pdf"
    context = {
        "title": "Awesome Project",
    }

    fill_svg(
        template_path,
        output_svg_path,
        context,
    )

    system(
        f"{inkscape} --export-type=pdf "
        f"--export-filename={output_path} {output_svg_path}"
    )
