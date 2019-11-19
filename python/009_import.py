import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='version_arg', type=int)
parsed_args = parser.parse_args()
VERSION = parsed_args.version_arg or 1

'''
import
        make files string.py, random.py, make random.choice(string.letters) do something else



'''

if VERSION == 1:

