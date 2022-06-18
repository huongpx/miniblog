FROM python:3.9.9-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONIOENCODING 'utf-8'

ENV GIT_PYTHON_REFRESH 'quiet'
ENV GIT_DISCOVERY_ACROSS_FILESYSTEM 1

ENV PYTHONPATH "/opt/app/python:$PYTHONPATH"
ENV PATH "/opt/app/bin:$PATH"

RUN /usr/local/bin/python -m pip install --upgrade pip
COPY ./requirements.txt /tmp/requirements.txt
RUN cd /tmp \
    && pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

RUN mkdir -p \
    /opt/app/python

COPY ./src /opt/app/python

WORKDIR /opt/app/python

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
