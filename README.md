# Vimwiki extensions

## Prerequisites
* poetry
* for development:
  * shellcheck

## Installation

    ./run.sh test

## Usage

Install this package the environment that you use to start
your vimwiki in. Currently this is simply done by using the
local package, e.g. by running:

```sh
poetry build
export VERSION=$(poetry version | awk '{print $2}')
pyenv activate <YOUR_ENV>
pip install dist/vimwiki_extensions-"$VERSION"-py3-none-any.whl
```

There is also a dependency to the vimwiki vim config: We call the python modules
specifically from the vim cmd, which is why the shebang is required at the top
of the file.


## Todo
* [ ] make this a library where user specific stuff is stored locally and gitignored:
  * [ ] DAY_SPECIFIC todos shouldnt be commited
* [ ] make sure mypy is used everywhere
* [ ] dont call the modules from vim, but use the env commands
