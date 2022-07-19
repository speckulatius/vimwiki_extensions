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
import generate_vimwiki_diary_template_work


TEST_PATH = Path(Path.cwd() / "tests/data/")


@pytest.fixture(autouse=True)
def override_config(monkeypatch):
    """Override path to vimwiki files."""
    monkeypatch.setitem(
        generate_vimwiki_diary_template_work.CONFIG, "WIKI_PATH", "/tmp"
    )


class TestRenderTemplate:
    @pytest.fixture
    def render_template(self):
        from generate_vimwiki_diary_template_work import render_template

        return render_template

    @pytest.fixture
    def tpl(self):
        from generate_vimwiki_diary_template_work import TEMPLATE

        return TEMPLATE

    def test_regular_monday(self, render_template, tpl):
        # given
        monday = datetime.strptime("20200720", "%Y%m%d")

        # when
        template = render_template(monday)
        # then
        assert template == tpl.format(diary_title=str(monday))

    def test_regular_friday(self, render_template, tpl):
        # given
        friday = datetime.strptime("20200828", "%Y%m%d")

        # when
        template = render_template(friday)

        # then
        tpl = tpl.format(diary_title=str(friday))
        tpl += "* [ ] make backup"
        assert template == tpl

    def test_copies_open_todos_from_previous_entry(self, render_template, monkeypatch):
        # given
        monkeypatch.setitem(
            generate_vimwiki_diary_template_work.CONFIG, "WIKI_PATH", TEST_PATH
        )
        monday = datetime.strptime("20200720", "%Y%m%d")

        # when
        template = render_template(monday)

        # then
        split_template = template.split("\n")
        assert "* [ ] review MR" in split_template
        assert "* [ ] fix tests" in split_template

    def test_gets_indentation_of_previous_todos_right(
        self, render_template, monkeypatch
    ):
        # given
        monkeypatch.setitem(
            generate_vimwiki_diary_template_work.CONFIG, "WIKI_PATH", TEST_PATH
        )
        monday = datetime.strptime("20200720", "%Y%m%d")

        # when
        template = render_template(monday)

        # then
        split_template = template.split("\n")
        assert "    * [ ] make it work" in split_template
        assert "    * [ ] remove harcoded tag" in split_template


class TestGetLastEntry:
    @pytest.fixture
    def get_last_entry(self):
        from generate_vimwiki_diary_template_work import get_last_entry

        return get_last_entry

    def test_get_last_entry(self, get_last_entry, monkeypatch):
        monkeypatch.setitem(
            generate_vimwiki_diary_template_work.CONFIG, "WIKI_PATH", TEST_PATH
        )
        assert get_last_entry() == "1950-01-01"

    def test_no_entries_exists(self, get_last_entry):
        with pytest.raises(FileNotFoundError):
            # pylint: disable=unused-variable
            prev_entry_date = get_last_entry()
