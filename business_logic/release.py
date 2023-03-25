
import os

from business_logic.validate import validate_news
from util.util import run, print_log, binary_prompt
from util.constants import TEST_VERSION, GITHUB_REPO, REPO, PYTHON3_WRAPPER
from util.shortlog_author_comparison import *

def verify_change_log_prerequisites():
  warnings = []
  if validate_news(warnings) != True:
    print("Change log issues found:")
    print_log(warnings)
    if not binary_prompt("Are you sure you wanna proceed?"):
      raise Exception("program terminated upon warnings")

def prepare_environment():
  print("Preparing release environment...")
  run(["pip3", "install", "re-ver"])

def clone_repo():
  print("Cloning Conda repo...")
  run(["git", "clone", GITHUB_REPO])
  
def initialize_release_branch(version):
  print("Initializing release branch...")
  run(["python3", "-m", "rever", "check"])
  run(["git", "checkout", "-b", version])

def aggregate_authors(version):
  print("Aggregating authors...")
  run(PYTHON3_WRAPPER + ["rever", "--activities", "authors", "--force", version])

def generate_change_log(version):
  print("Preparing change log...")
  run(PYTHON3_WRAPPER + ["rever", "--activities", "changelog", "--force", version])

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
    prepare_environment()
    clone_repo()
    os.chdir(dir + "/" + REPO)
    verify_change_log_prerequisites()
    initialize_release_branch(TEST_VERSION)
    aggregate_authors(TEST_VERSION)
    shortlog_author_comparison()
    generate_change_log(TEST_VERSION)
    push_to_remote(TEST_VERSION)
  finally:
    os.chdir(dir)
    clean_up()
