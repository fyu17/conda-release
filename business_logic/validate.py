import os
import re

from business_logic.commit import get_commits_since_last_release
from util.constants import REPO, TEMPLATE, NEWS_TITLE_PATTERN, COMMIT_MESSAGE_PATTERN, WARNING

def validate_arguments(args):
  if args.dir == "":
    print("Use current working directory by default")
  
  dir = os.getcwd() if args.dir == "" else os.path.abspath(args.dir)
  if os.path.isdir(f"{os.path.abspath(dir)}/{REPO}"):
    raise Exception("can't clone remote repo, there is already a directory named " + REPO)

# validate if there are missing news
# assume that current working directory is conda/
def validate_news(warnings: list):
  commits = get_commits_since_last_release()
  files = os.listdir(os.getcwd() + "/news")
  news = [file for file in files if file != TEMPLATE]

  prs_with_news = []
  for news_entry in news:
    match = re.match(NEWS_TITLE_PATTERN, news_entry)
    if match == None:
      warnings.append(WARNING + f"news entry: \"{news_entry}\" should have format \"{NEWS_TITLE_PATTERN}\"")
    else:
      prs_with_news.append(match.group(1))

  prs = []
  for commit_message in [commit[1] for commit in commits]:
    match = re.match(COMMIT_MESSAGE_PATTERN, commit_message)
    if match == None:
      warnings.append(WARNING + f"commit message: \"{commit_message}\" should have format \"{COMMIT_MESSAGE_PATTERN}\"")
    else:
      prs.append(match.group(1))
  
  prs_without_news = set(prs).difference(set(prs_with_news))
  warnings += [WARNING + f"PR https://github.com/conda/conda/pull/{pr} doesn't have a news" for pr in prs_without_news]
  is_valid = len(warnings) == 0

  return is_valid
