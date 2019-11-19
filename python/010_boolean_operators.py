import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='version_arg', type=int)
parsed_args = parser.parse_args()
VERSION = parsed_args.version_arg or 1

'''
var1 = 1 == 1
var1 = 1 + 1
type(1+1)
type(1==1)
print(1 > 2)
print(1 < '2')
'''

if VERSION == 1:

