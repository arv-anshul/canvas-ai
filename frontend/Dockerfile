FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

RUN --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
  uv sync --no-cache --no-dev

ADD . /app

CMD ["uv", "run", "--locked", "streamlit", "run", "app.py"]
