#!/home/jan/.pyenv/shims/python

"""
When run, this module prints out a template for a diary entry.

It is used whenever I create a new diary entry in my vimwiki (see
init.vim config).
"""

import calendar
import datetime
import os
import re
from functools import partial
from pathlib import Path


CONFIG = {"WIKI_PATH": Path("/home/jan/vimwikis/work/pit/")}
DAY_ITEMS = {
    "friday": ["make backup"],
    "monday": ["Read FT protocoll"],
}
TEMPLATE = """# {diary_title}


## Notes


## Todo

* [ ] Arbeitszeiten nachtragen
* [ ] Striche"""


def is_day(date: datetime.date, weekday: int) -> bool:
    """Given a date and weekday, this function returns whether
    the date is that specific weekday or not."""
    return date.weekday() == weekday


is_monday = partial(is_day, weekday=0)
is_friday = partial(is_day, weekday=4)


def is_open_todo(line: str) -> bool:
    """Based on the presence of certain symbols, checks whether
    a string is an open todo item or not
    """
    open_todo_symbols = [
        "* [ ]",
        "* [o]",
        "* [.]",
        "* [O]",
    ]
    if any(symbol in line for symbol in open_todo_symbols):
        return True
    return False


def get_open_todos(prev_entry: str) -> list:
    """
    Checks diary entry from previous (week)day for open
    todos and returns all that it finds.
    """
    lines = prev_entry.split("\n")
    open_todos = []
    for line in lines:
        if is_open_todo(line):
            open_todos.append(line)

    return open_todos


def get_last_entry() -> str:
    """Find last diary entry in a given directory. This assumes
    the filenames to correspond to a specific date pattern."""

    date_pattern = r"^\d{4}-\d{2}-\d{2}"
    files = [f for f in os.listdir(CONFIG["WIKI_PATH"]) if re.match(date_pattern, f)]

    try:
        return sorted(files)[-1].split(".")[0]
    except IndexError:
        # pylint: disable=raise-missing-from
        raise FileNotFoundError("No previous entries")


def add_day_specific_items(template: str, day: datetime.date) -> str:
    """
    Look up items for a specific day in a dictionary and append them to
    a passed template.
    """
    tpl = template
    day_string = calendar.day_name[day.weekday()].lower()

    try:
        for todo in DAY_ITEMS[day_string]:
            tpl += f"\n* [ ] {todo}"
        tpl += "\n"
    except KeyError:
        pass
    return tpl


def render_template(date: datetime.date) -> str:
    """
    For a given date, print out a diary template.

    The template is currently being customized based on the date and
    the contents of the previous weekday's diary-content.

    To work with vimwiki, the template simply needs to be printed out
    (not returned).
    """
    tpl = TEMPLATE
    diary_title = date

    tpl = add_day_specific_items(tpl, date)

    # load previous diary entry and check for open todos
    try:
        prev_entry_date = get_last_entry()
        with open(CONFIG["WIKI_PATH"] / f"{prev_entry_date}.md", "r") as diary_file:
            prev_entry = diary_file.read()
        open_todos = get_open_todos(prev_entry)
    except FileNotFoundError:
        open_todos = []

    # add any open todos to todays entry
    if len(open_todos) > 0:
        tpl += f"\n\n\n### leftovers from {prev_entry_date}\n"
        for todo in open_todos:
            tpl += f"\n{todo}"

    return tpl.format(diary_title=diary_title)


if __name__ == "__main__":
    template_rendered = render_template(datetime.date.today())
    print(template_rendered)
