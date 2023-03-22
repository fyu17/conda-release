import argparse

from business_logic.release import *
from business_logic.validate import *

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Automation script that creates release branches for Conda project.")
  parser.add_argument("-d", "--dir", metavar="Target Directory", help="Target directory (use current working directory by default)", type=str, default="")
  args=parser.parse_args()

  try:
    validate_arguments(args)
    create_release_branch(args)
  except Exception as e:
    print("Abort: " + str(e))
