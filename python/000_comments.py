import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-v', action='store', dest='version_arg', type=int)
parsed_args = parser.parse_args()
VERSION = parsed_args.version_arg or 1

if VERSION == 1:
    # this is a comment
    # python ignores everything after the number sign
    # print('a')
    print('b')

elif VERSION == 2:
    '''this is a string
    it has three quotes, so it can be
    used as a multi-line comment'''
    '''print('a')
    print('b')
    '''
    print('c')

elif VERSION == 3:
    print('''you can also print out a
    string like this. most code will be on
    one line, but here the string and print take
    up multiple lines''')

elif VERSION == 4:
    print( # you can't print out this comment 
    # python doesn't read this part
    )


elif VERSION == 5: # comments can be used to explain what is happening in code
    '''tell the user that their favorite animal is great'''
    animal_var = input("What's your favorite animal? ") #ask the user their favorite animal
    # input() will leave behind a string of what the user types, and animal_var will point at that
    print(animal_var, 'is a great choice!') # print out that their animal is a great choice
