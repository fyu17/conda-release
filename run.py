import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-y", action='store_true')
args = parser.parse_args()
print(args.y)