#!/usr/bin/env python
"""
Module that is used to print out diary templates for my work wiki.
"""

import calendar
import datetime
import os
import re
from pathlib import Path
from typing import Generator

from utils import render

TEMPLATE_NAME = "diary_work"
CONFIG = {"WIKI_PATH": Path("/home/jan/vimwikis/work/byt")}
DAY_ITEMS = {
    "monday": ["Read FT protocoll"],
    "tuesday": ["Sync"],
    "thursday": ["Sync"],
    "friday": ["make backup"],
}


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
        # tpl += "\n"
    except KeyError:
        pass

    return tpl


def _get_last_entry() -> str:
    """Find last diary entry in a given directory. This assumes
    the filenames to correspond to a specific date pattern."""

    date_pattern = r"^\d{4}-\d{2}-\d{2}"
    files = [
        f for f in os.listdir(CONFIG["WIKI_PATH"])
        if re.match(date_pattern, f)
    ]

    try:
        return sorted(files)[-1].split(".")[0]
    except IndexError:
        # pylint: disable=raise-missing-from
        raise FileNotFoundError("No previous entries")


def _is_open_todo(line: str) -> bool:
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


def _get_open_todos(entry: str) -> Generator:
    """Checks diary entry for open todos and returns all that it finds."""
    lines = entry.split("\n")

    for line in lines:
        if _is_open_todo(line):
            yield line


def add_open_todos(template: str) -> str:
    """
    Append any open todos from the previous diary entry and return it.
    """
    # load previous diary entry and check for open todos
    try:
        prev_entry_date = _get_last_entry()
        with open(CONFIG["WIKI_PATH"] / f"{prev_entry_date}.md",
                  "r") as diary_file:
            prev_entry = diary_file.read()
        open_todos = list(_get_open_todos(prev_entry))
    except FileNotFoundError:
        open_todos = []
        prev_entry_date = None

    # add any open todos to todays entry

    if len(open_todos) > 0 and prev_entry_date:
        template += f"\n\n\n### leftovers from {prev_entry_date}\n"

        for todo in open_todos:
            template += f"\n{todo}"

    return template


if __name__ == "__main__":
    today = datetime.date.today()

    rendered = render(TEMPLATE_NAME, today)
    items_added = add_day_specific_items(rendered, today)
    todos_added = add_open_todos(items_added)

    print(todos_added)
