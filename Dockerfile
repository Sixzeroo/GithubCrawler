FROM python:3.5

RUN mkdir /code

COPY ./requirements.txt /requirements.txt
COPY ./pip.conf /etc/pip.conf

WORKDIR /code

RUN pip install -r /requirements.txt

