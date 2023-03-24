from util.util import output

def get_latest_release():
  return output(["git", "describe", "--abbrev=0", "--tags"]).strip()

# Return a list of commits since last release
# Each commit entry represented by a list should have the form [<hash>, <commit message>]
def get_commits_since_last_release():
  prev_tag = get_latest_release()
  entries = output(["git", "cherry", "-v", prev_tag]).split("\n")[:-1]
  commits = [str(entry).split(None, 2)[1:] for entry in entries]
  return commits
