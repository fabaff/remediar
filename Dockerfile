FROM python:3.7.4-alpine3.10
MAINTAINER Fabian Affolter <fabian@affolter-engineering.com>
ENV PS1="\[\e[0;33m\]|> remediar <| \[\e[1;35m\]\W\[\e[0m\] \[\e[0m\]# "

ENV LANG C.UTF-8

RUN apk add --no-cache \
        make \
        python3 \
        git \
        glib-dev \
        gcc \
        libstdc++ \
        g++ \
        python3-dev

WORKDIR /src
COPY . /src
RUN pip install --no-cache-dir -r requirements.txt \
    && python setup.py install
WORKDIR /
ENTRYPOINT ["remediar"]
