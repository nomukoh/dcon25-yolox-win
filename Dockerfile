FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu20.04

# Set environment variables
ENV NOTO_DIR=/usr/share/fonts/opentype/notosans

# Update and install required packages
RUN apt update \
    && apt install -y \
    wget \
    bzip2 \
    git \
    curl \
    unzip \
    file \
    xz-utils \
    sudo \
    python3 \
    python3-pip \
    && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install NotoSans font
RUN mkdir -p ${NOTO_DIR} \
    && wget -q https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip -O noto.zip \
    && unzip ./noto.zip -d ${NOTO_DIR}/ \
    && chmod a+r ${NOTO_DIR}/NotoSans* \
    && rm ./noto.zip

# Install Python dependencies
COPY requirements.txt /tmp/
RUN python3 -m pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r /tmp/requirements.txt

# Clean up
RUN apt-get autoremove -y && apt-get clean && rm -rf /usr/local/src/*
