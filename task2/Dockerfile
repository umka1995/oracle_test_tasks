# Dockerfile

# Используем базовый образ Python
FROM python:3.9

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости и устанавливаем их
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем проект в контейнер
COPY . /app/

# Запускаем команду для старта сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

