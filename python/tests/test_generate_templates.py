"""Contains tests for template generating functions"""

from datetime import datetime
from pathlib import Path
import sys
sys.path.append('../python')

import pytest

TEST_PATH = Path("/home/jan/personal/utils/python/tests/data/")
TEMPLATE = """# {diary_title}


## Notes



## Todo

* [ ] Arbeitszeiten nachtragen
* [ ] Striche
"""

class TestDiaryTemplate:
    @pytest.fixture
    def render_template(self):
        from generate_vimwiki_diary_template_work import render_template

        return render_template

    def test_regular_monday(self, render_template):
        # given
        monday = datetime.strptime('20200720', '%Y%m%d')

        # when
        template = render_template(monday, wiki_path=TEST_PATH)

        # then
        assert template == TEMPLATE.format(diary_title="")

    def test_regular_friday(self, render_template):
        pass

    def test_copies_open_todos_from_previous_entry(self, render_template):
        pass

    def test_gets_indentation_of_previous_todos_right(self, render_template):
        pass
