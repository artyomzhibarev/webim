FROM python:3.9.4

ARG BUILD_PACKAGES="gcc g++ software-properties-common apt-transport-https apt-utils gnupg1 libcurl4-openssl-dev libssl-dev git-core"

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN set -ex && \
    apt-get update && \
    apt-get install -y --no-install-recommends $BUILD_PACKAGES && \
    rm -rf /var/lib/apt/lists/*

RUN set -ex && \
    pip3 install --upgrade pip

COPY ./requirements.txt /code/
COPY docker-entrypoint.sh /docker-entrypoint.sh

RUN pip3 install -r requirements.txt

RUN chmod +x /docker-entrypoint.sh

COPY . /code/

ENTRYPOINT ["sh", "/docker-entrypoint.sh"]