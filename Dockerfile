FROM python:3.12.4-slim

WORKDIR /code

# Install missing libs
RUN apt-get  update

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Install gunicorn
RUN pip install --upgrade pip && \
    pip install gunicorn gunicorn[gevent]

# Install poetry \
RUN pip install poetry

COPY poetry.lock pyproject.toml /code/

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the rest of the code
COPY . /code/

# Exposing Ports
EXPOSE 8000

# Environemnt variables
ENV DJANGO_SETTINGS_MODULE=config.settings GUNICORN_BIND=0.0.0.0:8000 GUNICORN_WORKERS=4 GUNICORN_THREADS=2 GUNICORN_TIMEOUT=300 GUNICORN_LOG_LEVEL=info

# Running Python Application
CMD bash startup.sh