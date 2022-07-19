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
import print_diary_work


TEST_PATH = Path(Path.cwd() / "tests/data/")


@pytest.fixture(autouse=True)
def override_config(monkeypatch):
    """Override path to vimwiki files."""
    monkeypatch.setitem(
        print_diary_work.CONFIG, "WIKI_PATH", "/tmp"
    )



class TestRenderTemplate:
    @pytest.fixture
    def render(self):
        from utils import render
        return render

    @pytest.fixture
    def add_open_todos(self):
        from print_diary_work import add_open_todos
        return add_open_todos

    @pytest.fixture
    def tpl_name(self):
        return 'diary_privat'

    @pytest.fixture
    def old_entry(self):
        with open(f'{TEST_PATH}/1900-01-01.md', 'r') as f:
            entry = f.read()
        return entry

    @pytest.fixture
    def new_entry(self):
        with open(f'{TEST_PATH}/1950-01-01.md', 'r') as f:
            entry = f.read()
        return entry

    @pytest.fixture
    def dummy_tpl(self):
        return 'foo'

    def test_copies_open_todos_from_previous_entry(self, monkeypatch, add_open_todos, dummy_tpl):
        # given
        monkeypatch.setitem(
            print_diary_work.CONFIG, "WIKI_PATH", TEST_PATH
        )
        monday = datetime.strptime("20200720", "%Y%m%d")
        # when
        template = add_open_todos(dummy_tpl)
        # then
        split_template = template.split("\n")
        assert "* [ ] review MR" in split_template
        assert "* [ ] fix tests" in split_template

#######################################################################
################        WIP       #####################################
#######################################################################

    def test_gets_indentation_of_previous_todos_right(
        self, render, monkeypatch
    ):
        # given
        monkeypatch.setitem(
            print_diary_work.CONFIG, "WIKI_PATH", TEST_PATH
        )
        monday = datetime.strptime("20200720", "%Y%m%d")

        # when
        template = render(monday)

        # then
        split_template = template.split("\n")
        assert "    * [ ] make it work" in split_template
        assert "    * [ ] remove harcoded tag" in split_template

    def test_no_blank_line_at_end(self, render, monkeypatch):
        monkeypatch.setitem(
            print_diary_work.CONFIG, "WIKI_PATH", TEST_PATH
        )

        monday = datetime.strptime("20200720", "%Y%m%d")

        # when
        template = render(monday)

        # then
        assert template[-1:] != "\n"


class TestGetLastEntry:
    @pytest.fixture
    def get_last_entry(self):
        from print_diary_work import get_last_entry

        return get_last_entry

    def test_get_last_entry(self, get_last_entry, monkeypatch):
        monkeypatch.setitem(
            print_diary_work.CONFIG, "WIKI_PATH", TEST_PATH
        )
        assert get_last_entry() == "1950-01-01"

    def test_no_entries_exists(self, get_last_entry):
        with pytest.raises(FileNotFoundError):
            # pylint: disable=unused-variable
            prev_entry_date = get_last_entry()


