#!/bin/bash
VERSION=0
if [ ${1:0:2} == '-v' ]; then
    VERSION=${1:2}
fi














if [ $VERSION == 1 ]; then
#   'pwd' means 'print working directory'
#   'directory' means folder
#   it tells you what folder you are in

    pwd # print the folder I'm in















elif [ $VERSION == 2 ]; then

#   'cd' means 'change directory'
#   it allows you to go into a folder

    pwd # print the folder I'm in
    cd animals # change directory into the desktop
    pwd # print the folder I'm in



















elif [ $VERSION == 3 ]; then

#   a single dot means the folder
#   that you are currently in. Two
#   dots means your parent folder

    pwd # print the folder I'm in

    cd animals # cd into Desktop
    pwd # print the folder I'm in

    cd . # cd into the folder I'm in
    pwd # print the folder I'm in

    cd .. # cd into the parent folder
    pwd # print the folder I'm in
















elif [ $VERSION == 4 ]; then 

#   If you're ever lost, type 'cd ~'

    cd /usr/bin # get lost
    pwd # print the folder I'm in

    cd ~ # cd into my home folder
    pwd # print the folder I'm in

    cd Desktop # cd into Desktop
    pwd # print the folder I'm in










elif [ $VERSION == 5 ]; then
#   use 'ls' or 'dir' to list
#   the files in the directory (folder)

    cd animals/mammals

    ls # mac/linux
    dir # windows



elif [ $VERSION == 6 ]; then
    cd animals
    cd mammals
    ls c*.py
    dir *.py







elif [ $VERSION == 7 ]; then
    cd animals
    cd mammals
    python3 dog.py # mac/linux
    # windows users would run 'py dog.py'

fi
