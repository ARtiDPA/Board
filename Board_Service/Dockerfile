FROM python:3.11-slim-bookworm

# Установка системных зависимостей + очистка в одном RUN
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev && \
    pip install --no-cache-dir --upgrade pip && \
    rm -rf /var/lib/apt/lists/*

# Создаем пользователя
RUN useradd --create-home appuser
WORKDIR /app

# Копируем зависимости отдельно для кэширования
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Удаляем ненужные зависимости
RUN apt-get purge -y --auto-remove gcc python3-dev

USER appuser

# Указываем правильный путь к приложению
CMD ["uvicorn", "board_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
