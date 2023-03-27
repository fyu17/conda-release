import subprocess

def run(command, shell=False):
    subprocess.run(command, stdout=subprocess.DEVNULL, check=True, shell=shell)

def output(command,shell=False):
  return subprocess.check_output(command,shell=shell).decode("utf-8")

def print_log(logs):
  for log in logs:
    print(log)

def binary_prompt(question):
  answer = None
  while answer == None or answer not in ["Yes", "No"]:
    answer = input(question + " (Yes/No):")
  return answer == "Yes"
