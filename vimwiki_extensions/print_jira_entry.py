#!/usr/bin/env python
"""
This module prints out templates for when I create entries for
Jira stories.
"""

import sys

from utils import render

TEMPLATE_NAME = "jira_entry"


def get_vimwiki_filename():
    """Reads filename and returns it. Used here to get name of Jira Tag."""
    try:
        return sys.argv[1].split("/")[-1].split(".")[0]
    except IndexError:
        return "Task name"


if __name__ == "__main__":
    title = get_vimwiki_filename()
    rendered = render(TEMPLATE_NAME, title)
    print(rendered)
