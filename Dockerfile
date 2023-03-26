FROM python:3.8
ARG NAME
ARG EMAIL
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git
RUN git config --global user.name "${NAME}"
RUN git config --global user.email "${EMAIL}"
WORKDIR /conda-release
COPY . /conda-release
CMD python3 main.py