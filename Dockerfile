FROM python:3.7-slim-stretch

# Install missing libs
RUN apt-get  update \
    && apt-get install -y  curl libpq-dev gcc python3-cffi git && \
apt-get clean autoclean && \
apt-get autoremove --purge -y && \
rm -rf /var/lib/apt/lists/* && \
rm -f /var/cache/apt/archives/*.deb

# Creating Application Source Code Directory
RUN mkdir -p /usr/app

# Setting Home Directory for containers
WORKDIR /usr/app

# Installing python dependencies
COPY requirements.txt /usr/app
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Cleanup
RUN rm -rf /var/lib/apt/lists/*
RUN rm -rf /root/.cache/*
RUN rm -rf /tmp/*
RUN apt-get -y autoremove --purge && apt-get -y autoclean && apt-get -y clean
RUN rm -rf /usr/share/man/*
RUN rm -rf /usr/share/doc/*
RUN find /var/lib/apt -type f | xargs rm -f
RUN find /var/cache -type f -exec rm -rf {} \;
RUN find /var/log -type f | while read f; do echo -ne '' > $f; done;

# Copying src code to Container
COPY . /usr/app
RUN pip install --no-cache-dir -r requirements.txt

# Exposing Ports
EXPOSE 8000

# Environemnt variables
ENV DJANGO_ENV  development
ENV GUNICORN_BIND  0.0.0.0:8000
ENV GUNICORN_WORKERS 4
ENV GUNICORN_WORKERS_CONNECTIONS 1001

# Running Python Application
CMD python manage.py runserver 0.0.0.0:8000
#CMD gunicorn --workers=${GUNICORN_WORKERS} config.wsgi:application -b ${GUNICORN_BIND} --log-level info
