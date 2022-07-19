FROM python:3.8.1-slim-buster as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.0.5

RUN apt-get update && \
        # apt-get install -y --no-install-recommends build-essential gcc bzip2 curl ca-certificates && \
    pip install "poetry==$POETRY_VERSION"
