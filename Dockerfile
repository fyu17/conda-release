FROM ubuntu:20.04
ARG SSH_PRV_KEY
RUN apt-get update && \
    apt-get upgrade -y
RUN apt-get install -y git
RUN apt-get install -y python3 && \
    apt-get install -y python3-pip
RUN pip3 install re-ver
# config ssh
RUN mkdir -p /root/.ssh && \
    chmod 700 /root/.ssh
RUN echo "$SSH_PRV_KEY" > /root/.ssh/id_rsa && \
    chmod 400 /root/.ssh/id_rsa
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts
WORKDIR /conda-release 
COPY . /conda-release
ENTRYPOINT ["python3", "main.py", "-y"]
