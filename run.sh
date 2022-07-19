#!/bin/bash
set -eou pipefail
# set -x


if [[ $# -lt 1 ]]; then
  echo "Usage: $0 format | lint" >&2
  exit 1
fi


task_format_python() {
  black python/*
}


task_lint() {
  shellcheck ./*.sh
  pylint python/*
}


cmd=$1
case "$cmd" in
  format) task_format_python ;;
  lint) task_lint ;;
esac
