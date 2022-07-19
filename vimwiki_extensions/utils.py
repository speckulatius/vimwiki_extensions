"""Contains utility functions for vimwiki templates"""

from pathlib import Path

import jinja2
import toml

HERE = Path(__file__).parent
TEMPLATE_PATH = Path(HERE / "templates")
CONFIG_PATH = Path(HERE / "config.toml")


def render(template_name, title):
    """
    Render a jinja2 template.
    """
    template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATE_PATH)
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(f"{template_name}.jinja")
    return template.render(title=title)


def get_config():
    if not CONFIG_PATH.is_file():
        raise FileNotFoundError(
            f"No configuration file found at: {CONFIG_PATH}")

    with open(CONFIG_PATH, "r") as f:
        config = toml.load(f)

    return config
