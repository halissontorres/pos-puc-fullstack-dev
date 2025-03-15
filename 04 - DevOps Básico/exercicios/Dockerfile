FROM ubuntu:24.10

LABEL org.opencontainers.image.title="Ubuntu image" \
      org.opencontainers.image.description="A lightweight Ubuntu image" \
      org.opencontainers.image.version="1.0.0" \
      org.opencontainers.image.licenses="MIT" \
      org.opencontainers.image.source="https://github.com/halissontorres/pos-puc-fullstack-dev" \
      org.opencontainers.image.authors="halisson[dot]torres[at]gmail[dot]com"

RUN apt-get update --fix-missing && \ 
    apt-get install -y curl && \
    apt-get install -y net-tools && \
    apt autoclean && \
    apt autoremove && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*
    