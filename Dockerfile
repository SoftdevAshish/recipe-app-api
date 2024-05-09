FROM python:3.9-alpine3.13
LABEL maintainer="Ashish"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /temp/requirements.txt
COPY ./requirements.dev.txt /temp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN pip install --upgrade pip && \
    pip install -r /temp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then pip install -r /temp/requirements.dev.txt ; \
    fi && \
    rm -rf /temp && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user


ENV PATH="/djangorestframework/bin:$PATH"
USER django-user
