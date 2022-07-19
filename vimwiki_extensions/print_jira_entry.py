#!/usr/bin/env python

import sys

from utils import render


def get_vimwiki_filename():
    """Reads filename and returns it. Used here to get name of Jira Tag."""
    try:
        return sys.argv[1].split("/")[-1].split(".")[0]
    except IndexError:
        return "Task name"


if __name__ == "__main__":
    template_name = "jira_entry"
    title = get_vimwiki_filename()
    rendered = render(template_name, title)
    print(rendered)
