FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

COPY pyproject.toml .
RUN uv sync --no-cache --no-dev

ADD . /app

CMD ["uv", "run", "--locked", "uvicorn", "--host", "0.0.0.0", "--port", "8080", "app.main:app"]
