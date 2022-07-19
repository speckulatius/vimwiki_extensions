"""Contains tests for template generating functions"""
# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=wrong-import-position
# pylint: disable=import-outside-toplevel
# pylint: disable=no-self-use

from pathlib import Path
import sys

import pytest

sys.path.append("../vimwiki_extensions")
import print_diary_work

TEST_PATH = Path(Path.cwd() / "tests/data/")


@pytest.fixture(autouse=True)
def override_config(monkeypatch):
    """Override path to vimwiki files."""
    monkeypatch.setitem(print_diary_work.CONFIG, "WIKI_PATH", "/tmp")


class TestDiaryWorkFunctions:
    @pytest.fixture
    def add_open_todos(self):
        from print_diary_work import add_open_todos

        return add_open_todos

    @pytest.fixture
    def add_day_specific_items(self):
        from print_diary_work import add_day_specific_items

        return add_day_specific_items

    @pytest.fixture
    def is_open_todo(self):
        from print_diary_work import _is_open_todo

        return _is_open_todo

    @pytest.fixture
    def get_open_todos(self):
        from print_diary_work import _get_open_todos

        return _get_open_todos

    @pytest.fixture
    def get_last_entry(self):
        from print_diary_work import _get_last_entry

        return _get_last_entry

    @pytest.fixture
    def tpl_name(self):
        return "diary_privat"

    @pytest.fixture
    def old_entry(self):
        with open(f"{TEST_PATH}/1900-01-01.md", "r") as file:
            entry = file.read()
        return entry

    @pytest.fixture
    def new_entry(self):
        with open(f"{TEST_PATH}/1950-01-01.md", "r") as file:
            entry = file.read()
        return entry

    @pytest.fixture
    def dummy_tpl(self):
        return "foo"

    def test_copies_open_todos_from_previous_entry(self, monkeypatch,
                                                   add_open_todos, dummy_tpl):
        # given
        monkeypatch.setitem(print_diary_work.CONFIG, "WIKI_PATH", TEST_PATH)
        # when
        template = add_open_todos(dummy_tpl)
        # then
        split_template = template.split("\n")
        assert "* [ ] review MR" in split_template
        assert "* [ ] fix tests" in split_template
        assert "* [ ] check out this command: `rm -f foo_{1,2,3}`" in split_template

    def test_get_last_entry(self, get_last_entry, monkeypatch):
        monkeypatch.setitem(print_diary_work.CONFIG, "WIKI_PATH", TEST_PATH)
        assert get_last_entry() == "1950-01-01"

    def test_add_day_specific_items(self, add_day_specific_items):
        pass

    def test_is_open_todo(self, is_open_todo):
        pass
