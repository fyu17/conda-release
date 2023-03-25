import re
import subprocess


def shortlog_author_comparison():

    subprocess.run("git shortlog -se > shortlog.txt", shell=True, stdout=subprocess.DEVNULL, check=True)

    short_log_lst = []

    # Open the shortlog file for reading
    with open('shortlog.txt', 'r') as f:
        # Read the first line of the file
        line = " "
        while line:
            line = f.readline().strip().replace('\t', ' ')

            if line == "":
                continue

            # Split the first line into words
            words = line.split(" ")

            diff = 1
            for _ in reversed(words):
                if _.startswith('<'):
                    break
                diff += 1

            # Get the name from the split list
            name = " ".join(words[1:len(words)-diff])

            # Collect the name
            short_log_lst.append(name)

    short_log_lst.sort()

    #Process AUTHORS.md

    with open('AUTHORS.md', 'r') as f:
        text = f.read()

    # Find all the lines starting with an asterisk and extract the name
    authors_names = [re.findall(r'\* (.+)', line)[0] for line in text.split('\n') if line.startswith('*')]

    # Sort the names alphabetically
    authors_names.sort()

    diff = short_log_lst == authors_names

    diff_names = set(short_log_lst) - set(authors_names)

    if diff:
        print(f"Discrepancies detected: {list(diff_names)}")
    else:
        print(f"Shortlog names are the same as AUTHORS.md")

    #Duplicate Detection
    freq_dict = {}
    duplicates =[]
    for item in short_log_lst:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1

    for key, value in freq_dict.items():
        if value > 1:
            duplicates.append(key)

    if duplicates:
        print(f"Note: Duplicates found in short log {duplicates}")

    subprocess.run("rm shortlog.txt", shell=True, stdout=subprocess.DEVNULL, check=True)
    
    return diff

if __name__ == "__main__":
    shortlog_author_comparison()
