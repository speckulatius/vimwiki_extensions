#!/bin/bash


set -eou pipefail


if [[ $# -lt 1 ]]; then
  echo "Usage: $0 create-env | build | format | typing | lint | test | update | ci" >&2
  exit 1
fi

task_create_env() {
    poetry install
}

task_format_python() {
    task_create_env
    poetry run yapf --verbose -ir vimwiki_extensions/*
}

_task_check_typing() {
    echo "Running mypy..."
    poetry run mypy vimwiki_extensions/*.py
}

task_check_typing() {
    task_create_env
    _task_check_typing
}

_task_lint() {
    echo "Running shellcheck..."
    shellcheck ./*.sh
    echo "Running flake8..."
    poetry run flake8 --statistics --config .flake8 vimwiki_extensions
    echo "Running yapf..."
    poetry run yapf --diff -r vimwiki_extensions/*
}

task_lint() {
    task_create_env
    _task_lint
}

_task_test() {
    echo "Running pytest..."
    (cd vimwiki_extensions && poetry run pytest --cov "$@")
}

task_test() {
    task_create_env
    _task_test "$@"
}

task_ci() {
    task_create_env
    _task_lint
    _task_check_typing
    _task_test --cov-fail-under=70
}

task_update_dependencies() {
    poetry update
}

cmd=$1
shift || true
case "$cmd" in
  create-env) task_create_env ;;
  format) task_format_python ;;
  typing) task_check_typing;;
  lint) task_lint ;;
  test) task_test "$@";;
  update) task_update_dependencies ;;
  ci) task_ci ;;
esac
