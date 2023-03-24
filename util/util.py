import subprocess

def run(command):
  subprocess.run(command, stdout=subprocess.DEVNULL, check=True)

def output(command):
  return subprocess.check_output(command).decode("utf-8")

def print_log(logs):
  for log in logs:
    print(log)

def binary_prompt(question):
  answer = None
  while answer == None or answer not in ["Yes", "No"]:
    answer = input(question + " (Yes/No):")
  return answer == "Yes"
