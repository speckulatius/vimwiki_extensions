#!/bin/bash


set -eou pipefail


if [[ $# -lt 1 ]]; then
  echo "Usage: $0 create-env | build | format | lint | test | update | ci" >&2
  exit 1
fi

task_create_env() {
    poetry install
}

task_format_python() {
    task_create_env
    poetry run black vimwiki_extensions/*
}


task_lint() {
    task_create_env
    shellcheck ./*.sh
    poetry run pylint vimwiki_extensions/*
}

task_test() {
    task_create_env
    (cd vimwiki_extensions && poetry run py.test)
}

task_ci() {
    task_format_python
    task_lint
    task_test
}

task_update_dependencies() {
    poetry update
}

task_build_image() {
    task_ci
    docker build -t registry.gitlab.com/specktrum/vimwiki_extensions .
    docker push registry.gitlab.com/specktrum/vimwiki_extensions
}

cmd=$1
case "$cmd" in
  create-env) task_create_env ;;
  build) task_build_image ;;
  format) task_format_python ;;
  lint) task_lint ;;
  test) task_test ;;
  update) task_update_dependencies ;;
  ci) task_ci ;;
esac
