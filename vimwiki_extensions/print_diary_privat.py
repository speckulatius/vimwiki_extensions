#!/usr/bin/env python
"""
Module that is used to print out diary templates for my privat wiki.
"""

import datetime

from vimwiki_extensions.utils import render

TEMPLATE_NAME = "diary_privat"

if __name__ == "__main__":
    today = datetime.date.today()

    rendered = render(TEMPLATE_NAME, today)

    print(rendered)
