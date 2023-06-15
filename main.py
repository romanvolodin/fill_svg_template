from os import system
from pathlib import Path

from environs import Env


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

    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / "out.pdf"
    context = {
        "title": "Awesome Project",
    }

    fill_svg(
        "template/example.svg",
        "output/output.svg",
        context,
    )

    system(
        f"{inkscape} --export-type=pdf "
        f"--export-filename={output_path} output/output.svg"
    )
