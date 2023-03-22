import os

from util.constants import REPO

def validate_arguments(args):
  if args.dir == "":
    print("Use current working directory by default")
  
  dir = os.getcwd() if args.dir == "" else os.path.abspath(args.dir)
  if os.path.isdir(f"{os.path.abspath(dir)}/{REPO}"):
    raise Exception("can't clone remote repo, there is already a directory named " + REPO)
