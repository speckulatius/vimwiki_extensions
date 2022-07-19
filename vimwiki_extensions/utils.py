"""Contains utility functions for vimwiki templates"""

import datetime
from functools import partial
from pathlib import Path

import jinja2


DIRNAME = Path("/home/jan/personal/vimwiki_extensions/vimwiki_extensions")
TEMPLATE_PATH = Path(DIRNAME / "templates")


def is_day(date: datetime.date, weekday: int) -> bool:
    """Given a date and weekday, this function returns whether
    the date is that specific weekday or not."""
    return date.weekday() == weekday


is_monday = partial(is_day, weekday=0)
is_friday = partial(is_day, weekday=4)


def render(template_name, title):
    templateLoader = jinja2.FileSystemLoader(searchpath=TEMPLATE_PATH)
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(f"{template_name}.jinja")
    return template.render(title=title)
