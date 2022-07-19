#!/usr/bin/env python

import datetime

from utils import render


if __name__ == "__main__":
    template_name = "diary_privat"
    today = datetime.date.today()

    rendered = render(template_name, today)

    print(rendered)
