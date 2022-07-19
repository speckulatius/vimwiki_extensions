# Vimwiki extensions
Python package that I use together with [vimwiki](https://github.com/vimwiki/vimwiki)
to manage the templating of work diary entries. Main features are currently:
- Infer titles of entries based on date
- transfer open todo items from yesterday
- allow different templates to be used depending on the naming pattern of the file to be opened

## Prerequisites
* python
* poetry
* for development:
  * shellcheck

## Installation

    ./run.sh test

## Usage
Install this package in the environment that you use to start
your vimwiki in. Currently this is simply done by using the
local package, e.g. by running:

    poetry build
    export VERSION=$(poetry version | awk '{print $2}')
    pyenv activate <YOUR_ENV>
    pip install dist/vimwiki_extensions-"$VERSION"-py3-none-any.whl

To make use of the templates, I simply invoke a python module when a file with
a specific pattern is created. To do this, simply add a such as the following
to your init.vim configuration file:

    au BufNewFile ~/vimwikis/work/PROJECT/PROJECT_HANDLE-*.md :silent 0r !~/vimwikis/vimwiki_extensions/vimwiki_extensions/print_jira_entry.py '%'

## Todo
* [ ] move all logic to a single python module which takes an additional
      argument instead of copying modules around
* [ ] finish unit tests