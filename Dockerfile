FROM python:3.9.2-slim-buster AS speedo-compile
ENV PYTHONUNBUFFERED 1

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV TIMEZONE Europe/London

RUN mkdir /speedo
RUN mkdir /speedo/env

WORKDIR /speedo

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends \
        gcc \
        build-essential \
        python3-setuptools \
        python3-virtualenv \
        python3-pip \
    && pip3 install -U pip setuptools \
    && pip3 install --upgrade pip \
    && apt-get -y autoremove \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /speedo/env
ENV PATH="/speedo/env/bin:$PATH"

# keeping this here prevents container rebuilding on code changes
COPY ./requirements.txt ./

RUN pip3 install --upgrade pip \
    && pip3 install --upgrade setuptools \
    && pip3 install --no-cache-dir -r requirements.txt \
    && rm -rf /root/.cache \
    && apt-get autoremove -y

FROM python:3.9.2-slim-buster AS speedo-build

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8
ENV TIMEZONE Europe/London

COPY --from=speedo-compile /speedo /speedo
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y libmagic-dev \
    && apt-get -y autoremove \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /speedo/code
ENV PATH="/speedo/env/bin:$PATH"

ENTRYPOINT ["sh", "/speedo/code/entrypoint.sh"]
