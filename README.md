# Conda Release Branch Automation Tool

## Use Guide

### Docker
To build the image, run
```
docker build -t <image_name> --build-arg NAME=<git_name> --build-arg EMAIL=<git_email> --build-arg SSH_PRV_KEY="$(cat <path_to_ssh_private_key>)" .
```

Then, run the container in interactive mode:
```
docker run -it <image-name>
```

For example, 
```
$ docker build -t conda-release --build-arg NAME="Elon Musk" --build-arg EMAIL="elon.musk@email.com" --build-arg SSH_PRV_KEY="$(cat ~/.ssh/id_rsa)" .
$ docker run -it conda-release
```

### usage
main [-h] [-d Target Directory]

### arguments
- -h, --help show this help message and exit
- -d, --dir Target directory (use current working directory by default)

## Installation Guide
- Install pyinstaller: ```pip3 install pyinstaller```.
- Build executable using PyInstaller module: ```python3 -m PyInstaller main.py -F```.
- You can then find the excutable in the ```/dist``` directory.