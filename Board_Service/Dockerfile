# ----------------
# Build Stage
# ----------------
FROM python:3.12-slim-bookworm AS builder

# Установка системных зависимостей только для сборки
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev

# Создаем виртуальное окружение
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Установка зависимостей в виртуальное окружение
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ----------------
# Runtime Stage
# ----------------
FROM python:3.12-slim-bookworm

# Копируем виртуальное окружение из builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Создаем пользователя и рабочую директорию
RUN useradd --create-home appuser
WORKDIR /app
USER appuser

# Копируем только исходный код (без системных зависимостей)
COPY --chown=appuser:appuser . .

# Отключаем буферизацию логов Python
ENV PYTHONUNBUFFERED=1

# Порт приложения
EXPOSE 8000

# Команда запуска
CMD ["uvicorn", "board_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
