# # ============ STAGE 1: Builder Stage ============
# # Используем полный образ для сборки зависимостей
# FROM python:3.11-slim AS builder

# WORKDIR /app

# # Устанавливаем системные зависимости для сборки пакетов
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gcc \
#     g++ \
#     && rm -rf /var/lib/apt/lists/*

# # Копируем файл с зависимостями
# COPY requirements.txt .

# # Устанавливаем зависимости в отдельную директорию
# RUN pip install --user --no-cache-dir -r requirements.txt


# # ============ STAGE 2: Runtime Stage ============
# # Используем минимальный образ для выполнения
# FROM python:3.11-slim

# # Создаем непривилегированного пользователя (требование задания)
# RUN groupadd -r appuser && useradd -r -g appuser appuser

# WORKDIR /app

# # Копируем установленные зависимости из builder stage
# COPY --from=builder /root/.local /home/appuser/.local

# # Копируем исходный код приложения
# COPY . .

# # Устанавливаем права для непривилегированного пользователя
# RUN chown -R appuser:appuser /app

# # Переключаемся на непривилегированного пользователя
# USER appuser

# # Добавляем директорию с пакетами в PATH
# ENV PATH="/home/appuser/.local/bin:${PATH}"

# # Проверяем установку зависимостей
# RUN python -c "import flask; import redis; print('Dependencies verified')"

# # Открываем порт приложения
# EXPOSE 5000

# # Команда запуска
# CMD ["python", "app.py"]