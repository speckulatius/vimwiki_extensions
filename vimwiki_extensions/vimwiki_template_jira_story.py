#!/home/jan/miniconda3/bin/python

"""
When run, this module prints out a template for a Jira story entry.

It is used whenever I create a new entry in my vimwiki  for a Jira story (see
init.vim config).
"""


TEMPLATE = """# {jira_story_tag}


## Notes


## Todo


## Issues


## Questions"""


def get_jira_tag():
    """Reads filename and returns it. Used here to get name of Jira Tag."""
    return "PIT-XXXX"  # TODO: Return real jira tag


if __name__ == "__main__":
    print(TEMPLATE.format(jira_story_tag=get_jira_tag()))
