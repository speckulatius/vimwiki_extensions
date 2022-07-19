"""Contains utility functions for vimwiki templates"""

from pathlib import Path

import jinja2


DIRNAME = Path("/home/jan/privat/vimwiki_extensions/vimwiki_extensions")
TEMPLATE_PATH = Path(DIRNAME / "templates")


def render(template_name, title):
    """
    Render a jinja2 template.
    """
    template_loader = jinja2.FileSystemLoader(searchpath=TEMPLATE_PATH)
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(f"{template_name}.jinja")
    return template.render(title=title)
