import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='version_arg', type=int)
parsed_args = parser.parse_args()
VERSION = parsed_args.version_arg or 1

'''
list, string index
str always one char, list can be very big
slicing
.join
len()
['abcde']
'''

if VERSION == 1:

