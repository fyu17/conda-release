REPO = "conda"
GITHUB_REPO = "git@github.com:fyu17/conda.git"
PYTHON3_WRAPPER = ["python3", "-m"]
TEMPLATE = "TEMPLATE"
PR_BASE_ADDRESS = "https://github.com/conda/conda/pull/"
WARNING = "[WARNING]: "
USER_NAME = "Conda Bot"
EMAIL = "18747875+conda-bot@users.noreply.github.com"

# regular expressions
NEWS_TITLE_PATTERN = "(\\d+)-.*"
COMMIT_MESSAGE_PATTERN = ".*\\s+\\(#(\\d+)\\)"
VERSION_PATTERN = "[a-zA-Z0-9]+\\.[a-zA-Z0-9]+\\.[a-zA-Z0-9]+"

# Constants for testing
TEST_VERSION = "0.0.0"
