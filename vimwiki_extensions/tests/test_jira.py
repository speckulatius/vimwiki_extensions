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


TEST_PATH = Path(Path.cwd() / "tests/data/")


class TestRenderTemplateJira:
    @pytest.fixture
    def get_vimwiki_filename(self):
        from print_jira_entry import get_vimwiki_filename

        return get_vimwiki_filename

    def test_get_title(self, get_vimwiki_filename):
        # given
        jira_task = "PIT-1234"
        sys.argv.insert(1, jira_task)

        # when
        title = get_vimwiki_filename()

        # then
        assert title == jira_task
