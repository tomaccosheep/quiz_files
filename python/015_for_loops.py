import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='version_arg', type=int)
parsed_args = parser.parse_args()
VERSION = parsed_args.version_arg or 1

'''
everything that can be broken into pieces
str, list different pieces like index
range pieces, range how many times

'''

if VERSION == 1:

