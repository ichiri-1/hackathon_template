FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /workspace

COPY backend/pyproject.toml backend/uv.lock ./

RUN uv sync --no-dev --system --frozen

COPY backend/app ./app

CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT
