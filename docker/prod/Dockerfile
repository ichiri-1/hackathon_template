# マルチステージビルド
# フロントエンドビルド
FROM node:22-slim AS frontend

WORKDIR /app

COPY frontend/package*.json ./

RUN npm ci

COPY frontend/ ./

RUN npm run build


# バックエンド
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

WORKDIR /workspace

COPY backend/pyproject.toml backend/uv.lock ./

RUN uv sync --no-dev --frozen

COPY backend/app ./app
COPY --from=frontend /app/dist ./static

CMD ["sh", "-c", "uv run uvicorn app.main:app --host 0.0.0.0 --port $PORT"]
