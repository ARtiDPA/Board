#
# Build Stage
#
FROM python:3.12-alpine AS builder

RUN apk update && \
    apk add --no-cache \
        gcc \
        musl-dev \
        python3-dev

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#
# Runtime Stage
#
FROM python:3.12-alpine

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN adduser -D -h /home/appuser appuser
WORKDIR /app
USER appuser

COPY --chown=appuser:appuser app ./app

ENV PYTHONPATH=/app

ENV PYTHONUNBUFFERED=1
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
