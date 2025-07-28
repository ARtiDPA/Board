# Используем более свежий базовый образ с исправлениями безопасности
FROM python:3.12-slim-bookworm

# Устанавливаем только необходимые системные зависимости с очисткой в одном слое
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    pip install --no-cache-dir --upgrade pip && \
    rm -rf /var/lib/apt/lists/*

# Создаем пользователя с домашней директорией
RUN useradd --create-home appuser
WORKDIR /app

# Копируем зависимости отдельно для лучшего кэширования
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Удаляем build-зависимости в том же слое (для уменьшения размера и уязвимостей)
RUN apt-get purge -y --auto-remove gcc python3-dev && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Копируем исходный код
COPY . .

# Устанавливаем владельца файлов
RUN chown -R appuser:appuser /app
USER appuser

# Порт приложения
EXPOSE 8000

# Команда запуска с явным указанием пути
CMD ["uvicorn", "board_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
