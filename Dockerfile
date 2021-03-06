FROM python:3.9-slim

COPY src/ /usr/src/app/
WORKDIR /usr/src/app

RUN cp requirements.txt /tmp/ \
    && pip install --upgrade pip \
    && pip install -r /tmp/requirements.txt \
    && rm -r /tmp/*

EXPOSE 80

ENTRYPOINT []
CMD []

