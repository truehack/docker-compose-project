# Используем стандартный nginx без изменений
FROM nginx:alpine

# Удаляем дефолтный конфиг
RUN rm /etc/nginx/conf.d/default.conf

# Копируем наш конфиг
COPY nginx.conf /etc/nginx/conf.d/

# Копируем HTML файлы
COPY index.html /usr/share/nginx/html/

# НЕ меняем пользователя, запускаем как есть