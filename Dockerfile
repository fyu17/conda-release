FROM ubuntu:20.04
ARG NAME
ARG EMAIL
ARG SSH_PRV_KEY
ARG VERSION
RUN apt-get update && \
    apt-get upgrade -y
RUN apt-get install -y git
RUN apt-get install -y python3 && \
    apt-get install -y python3-pip
RUN pip3 install re-ver
# config git
RUN git config --global user.name "${NAME}"
RUN git config --global user.email "${EMAIL}"
# config ssh
RUN mkdir -p /root/.ssh && \
    chmod 700 /root/.ssh
RUN echo "$SSH_PRV_KEY" > /root/.ssh/id_rsa && \
    chmod 400 /root/.ssh/id_rsa
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts
WORKDIR /conda-release 
COPY . /conda-release
ENV VERSION_ENV="${VERSION}"
ENTRYPOINT python3 main.py -y "$VERSION_ENV"
