# ============ STAGE 1: Builder ============
FROM python:3.11-alpine AS builder

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt .
RUN pip install --prefix=/install --no-cache-dir -r requirements.txt


# ============ STAGE 2: Runtime ============
FROM python:3.11-alpine

RUN addgroup -S appuser && adduser -S appuser -G appuser

RUN mkdir -p /app && chown -R appuser:appuser /app

WORKDIR /app

COPY --from=builder /install /usr/local
COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 5000

CMD ["python", "app.py"]