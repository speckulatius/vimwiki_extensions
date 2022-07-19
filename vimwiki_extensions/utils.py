"""Contains utility functions for vimwiki templates"""

import datetime
from functools import partial
from pathlib import Path

import jinja2


DIRNAME = Path("/home/jan/privat/vimwiki_extensions/vimwiki_extensions")
TEMPLATE_PATH = Path(DIRNAME / "templates")


def render(template_name, title):
    templateLoader = jinja2.FileSystemLoader(searchpath=TEMPLATE_PATH)
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(f"{template_name}.jinja")
    return template.render(title=title)
