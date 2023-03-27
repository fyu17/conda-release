# Conda Release Branch Automation Tool

## Use Guide

### Docker
To build the image, run
```
docker build -t <image-name> --build-arg NAME=<your-github-name> --build-arg EMAIL=<yout-github-email> .
```

Then, run the container in interactive mode:
```
docker run -i <image-name>
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