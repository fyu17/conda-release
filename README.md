# Conda Release Branch Automation Tool

## Docker
Running in docker allows non-interactive (assuming yes) workflow, and is recommended.
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

## Local Usage
Running locally is also supported. Doing so requires that the current directory does NOT have a directory named "conda" since a clone of the conda repository is needed.

### Installation Guide
To run locally, the script needs to be installed.
- Install pyinstaller: ```pip3 install pyinstaller```.
- Build executable using PyInstaller module: ```python3 -m PyInstaller main.py -F```.
- You can then find the executable in the ```/dist``` directory.

After that, run the generated executable:
```
main [-h] [-d Target Directory] [-y]
```

### Arguments
-h, --help show this help message and exit \
-d, --dir Target directory (use current working directory by default) \
-y, --yes Automatic yes to prompts; assume "yes" as answer to all prompts and run non-interactively
