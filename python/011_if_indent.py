import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='version_arg', type=int)
parsed_args = parser.parse_args()
VERSION = parsed_args.version_arg or 1

'''
var1 = True
var2 = 1 == 1
if var1
if var2
if var1 and var2

if True:
    if False:
        print('a')
    print('b')

you set a rule with a colon
indented lines are subservient to a rule with a colon
a line of code can be indented under multiple rules
'''

if VERSION == 1:

