FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu18.04

ARG PYTHON_VERSION

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    cmake \
    git \
    curl \
    wget \
    vim \
    zip \
    unzip \
    ca-certificates \
    libjpeg-dev \
    libpng-dev \
    && rm -rf /var/lib/apt/lists/*

RUN curl -o ~/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && chmod +x ~/miniconda.sh \
    && ~/miniconda.sh -b -p /opt/conda \
    && rm ~/miniconda.sh

# Install PyTorch V1.
ENV PATH /opt/conda/bin:$PATH

RUN conda install -y python=$PYTHON_VERSION pyyaml

RUN conda install pytorch torchvision cudatoolkit=10.1 -c pytorch \
    && conda clean -ya

RUN pip install --no-cache-dir tensorboard

WORKDIR /home/src
