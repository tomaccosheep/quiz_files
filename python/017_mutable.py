import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='version_arg', type=int)
parsed_args = parser.parse_args()
VERSION = parsed_args.version_arg or 1

'''
mutable, immutable info
        return copy or leave behind none
                multiple references to the same info
                        use id()



'''

if VERSION == 1:

