import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='version_arg', type=int)
parsed_args = parser.parse_args()
VERSION = parsed_args.version_arg or 1

'''
input prints out whatever is in the parentheses
then it lets the user type stuff
then it leaves behind a string of what the user typed
'''


if VERSION == 1:
    var1 = input('type something: ')
    print(var1)

elif VERSION == 2:
    print('abc'*10)
    var1 = input('type something: ')
    print(var1*10)

elif VERSION == 3:
    print(input('type something: ')*10)

elif VERSION == 4:
    print(input('type something: '*10))

elif VERSION == 5:
    print(input('abcd'))

elif VERSION == 6:
    var1 = input('abcd')
    print(var1)

elif VERSION == 7:
    var1 = 'type something: '
    input(var1)
    print(var1)
