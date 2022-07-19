"""Contains tests for template generating functions"""
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=wrong-import-position
# pylint: disable=import-outside-toplevel
# pylint: disable=no-self-use

from datetime import datetime
from pathlib import Path
import sys

import pytest

sys.path.append("../vimwiki_extensions")
import utils


class TestRender:
    @pytest.fixture
    def render(self):
        from utils import render

        return render

    def test_render_privat(self, render):
        # given
        template_name = "diary_privat"
        title = "New shiny wiki entry"

        # when
        template = render(template_name, title)

        # then
        assert title in template
