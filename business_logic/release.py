
import os

from business_logic.validate import validate_news
from util.util import run, print_log, binary_prompt,output
from util.constants import GITHUB_REPO, REPO, PYTHON3_WRAPPER, USER_NAME, EMAIL
from util.shortlog_author_comparison import *

def verify_change_log_prerequisites(args):
  warnings = []
  if validate_news(warnings) != True:
    print("Change log issues found:")
    print_log(warnings)
    if not args.yes:
      if not binary_prompt("Are you sure you wanna proceed?"):
        raise Exception("program terminated upon warnings")

def prepare_environment():
  print("Preparing release environment...")
  # Impersonate Conda Bot to let rever know the Github username
  run(["git", "config", "user.name", USER_NAME])
  run(["git", "config", "user.email", EMAIL])

def clone_repo():
  print("Cloning Conda repo...")
  run(["git", "clone", GITHUB_REPO])
  
def initialize_release_branch(version):
  print("Initializing release branch...")
  run(PYTHON3_WRAPPER + ["rever", "check"])
  run(["git", "checkout", "-b", version])

def aggregate_authors(version):
  print("Aggregating authors...")
  run(PYTHON3_WRAPPER + ["rever", "--activities", "authors", "--force", version])

def author_commit():
  print("Commiting the .authors.yml")
  run("git reset --soft HEAD~1",shell=True)
  run("git restore --staged .mailmap AUTHORS.md", shell=True)
  run("git checkout .mailmap AUTHORS.md", shell=True)
  # Commit if work tree is not clean
  if output(["git", "diff", "HEAD"]) != "":
    run("git add .authors.yml", shell=True)
    run("git commit -m \"Updated .authors.yml\"",shell=True)

def mailmap_commit():
  print("Commiting the .mailmap")
  run("git reset --soft HEAD~1",shell=True)
  run("git restore --staged .authors.yml AUTHORS.md", shell=True)
  run("git checkout .authors.yml AUTHORS.md", shell=True)
  # Commit if work tree is not clean
  if output(["git", "diff", "HEAD"]) != "":
    run("git add .mailmap", shell=True)
    run("git commit -m \"Updated .mailmap\"",shell=True)
  

def generate_change_log(version):
  print("Preparing change log...")
  run(PYTHON3_WRAPPER + ["rever", "--activities", "changelog", "--force", version])
  run("git reset --hard HEAD~1", shell=True)
  run(PYTHON3_WRAPPER + ["rever", "--force", version])

def push_to_remote(version):
  print("Push release branch to remote...")
  run(["git", "push", "--force", "origin", version])

def clean_up():
  print("Cleaning up environment and artifacts...")
  run(["rm", "-rf", REPO])

def create_release_branch(args):
  dir = os.getcwd() if args.dir == "" else os.path.abspath(args.dir)
  try:
    os.chdir(dir)
    clone_repo()
    os.chdir(dir + "/" + REPO)
    prepare_environment()
    verify_change_log_prerequisites(args)
    initialize_release_branch(args.version)

    shortlog_author_same = False
    while not shortlog_author_same:
      aggregate_authors(args.version)
      author_commit()
      aggregate_authors(args.version)
      shortlog_author_same = shortlog_author_comparison()
      if not shortlog_author_same:
        print("Repeat the above process due to discrepancies")

    print("Mail map is correct now")
    mailmap_commit()
    generate_change_log(args.version)
    push_to_remote(args.version)
  finally:
    os.chdir(dir)
    clean_up()
