"""Contains tests for template generating functions"""
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=wrong-import-position
# pylint: disable=import-outside-toplevel
# pylint: disable=no-self-use

from pathlib import Path
import sys

import pytest

TEST_PATH = Path(Path.cwd() / "tests/data/")


class TestRenderTemplateJira:
    @pytest.fixture
    def get_vimwiki_filename(self):
        from print_jira_entry import get_vimwiki_filename

        return get_vimwiki_filename

    @pytest.mark.parametrize(
        "taskname",
        [
            ("AB-1234"),
            ("foo-12312"),
        ],
    )
    def test_get_title(self, taskname, get_vimwiki_filename):
        # given
        sys.argv.insert(1, taskname)

        # when
        title = get_vimwiki_filename()

        # then
        assert title == taskname


def remove_whitespace():
    pass


def remove_trailing_whitespace():
    pass
