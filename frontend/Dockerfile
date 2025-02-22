FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

COPY pyproject.toml .
RUN uv sync --no-cache --no-dev

ADD . /app

CMD ["uv", "run", "--locked", "streamlit", "run", "app.py"]
