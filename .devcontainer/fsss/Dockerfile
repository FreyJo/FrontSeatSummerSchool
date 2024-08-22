# Use an official Ubuntu image as a parent image
FROM ubuntu:20.04

WORKDIR /app

# Set time zone
RUN ln -fs /usr/share/zoneinfo/Europe/Berlin /etc/localtime

# Update the package list and install required packages
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    cmake \
    git \
    python3 \
    python3-pip \
    python3-tk \
    python3-dev \
    curl \
    libgfortran5 \
    gcc \
    gfortran \
    libopenblas-dev \
    && rm -rf /var/lib/apt/lists/

# Set the working directory
WORKDIR /app

# Install acados
# Clone and build acados
RUN git clone --depth 1 https://github.com/acados/acados.git \
    && cd acados \
    && git submodule update --recursive --init

RUN mkdir -p /app/acados/build
WORKDIR /app/acados/build
RUN cmake -DACADOS_INSTALL_DIR="/app/acados" .. \
    && make install -j4

## Tera should not needed to be built here.
# Install tera_renderer
# Install cargo for rust
RUN curl https://sh.rustup.rs -sSf > rustup.sh \
    && chmod +x rustup.sh \
    && ./rustup.sh -y \
    && rm rustup.sh

# Install tera_renderer
WORKDIR /app
RUN git clone https://github.com/acados/tera_renderer.git
RUN cd /app/tera_renderer \
    && ~/.cargo/bin/cargo build --verbose --bin t_renderer
RUN cp /app/tera_renderer/target/debug/t_renderer /app/acados/bin/t_renderer

# Set environment variables for using Acados in Python
ENV ACADOS_SOURCE_DIR /app/acados
ENV LD_LIBRARY_PATH $ACADOS_SOURCE_DIR/lib:$LD_LIBRARY_PATH

# Install python packages
RUN pip3 install --no-cache-dir scipy
RUN pip3 install --no-cache-dir numpy
# RUN pip3 install --no-cache-dir tqdm
RUN pip3 install --no-cache-dir matplotlib
RUN pip3 install --no-cache-dir jupyterlab
RUN pip3 install --no-cache-dir casadi
RUN pip3 install -e /app/acados/interfaces/acados_template
# Add further installations here as they are cached
RUN pip3 install --no-cache-dir future
# Add packages for SIPPY
RUN pip3 install --no-cache-dir control
RUN pip3 install scikit-build
RUN pip3 install setuptools_scm
RUN pip install -v slycot

# Add packages for Machine Learning tutorial
RUN pip3 install --no-cache-dir keras
