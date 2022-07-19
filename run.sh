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
    poetry run black vimwiki_extensions/*
}

_task_check_typing() {
    poetry run mypy vimwiki_extensions/*.py
}

task_check_typing() {
    task_create_env
    _task_check_typing
}

_task_lint() {
    shellcheck ./*.sh
    poetry run pylint vimwiki_extensions/*
    poetry run black vimwiki_extensions/* --check
}

task_lint() {
    task_create_env
    _task_lint
}

_task_test() {
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

task_build_image() {
    docker build -t registry.gitlab.com/specktrum/vimwiki_extensions .
    docker push registry.gitlab.com/specktrum/vimwiki_extensions
}

cmd=$1
shift || true
case "$cmd" in
  create-env) task_create_env ;;
  build) task_build_image ;;
  format) task_format_python ;;
  typing) task_check_typing;;
  lint) task_lint ;;
  test) task_test "$@";;
  update) task_update_dependencies ;;
  ci) task_ci ;;
esac
