import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='version_arg', type=int)
parsed_args = parser.parse_args()
VERSION = parsed_args.version_arg or 1

if VERSION == 1:
    # sometimes we'll make a variable point at something
    # in this case, it's pointing at a string
    # you can tell 'abc' is a string because it is in quotes
    # you can tell var1 is a variable because it is left of the equals sign
    var1 = 'abc'
    print(var1)

elif VERSION == 2:
    # this won't run, because a variable can't start
    # with a number
    '''
    2var = 'abc'
    print(2var)
    '''

elif VERSION == 3:
    # this won't run, because a variable can't have
    # a space in them
    '''
    var 1 = 'abc'
    print(var 1)
    '''

elif VERSION == 4:
    # you need to define your variables before you run them
    print(var1)
    var1 = 'abc'

elif VERSION == 5:
    # strings and variables can be confusing at first
    # I like to think that words in quotes point at themselves, and words not
    # in quotes point at other information
    # here we tell var1 to point at 'abc'
    var1 = 'abc'
    print(1, 'var1')  # this will print: 1, ______
    print(2, var1)  # this will print: 2, ______

elif VERSION == 6:
    left = 'right'
    right = 'left'
    up = 'down'
    down = 'up'
    print(1, left)
    print(2, 'right')
    print(3, 'up')
    print(4, down)
    print(5, 'down')
