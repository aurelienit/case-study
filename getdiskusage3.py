#Augustin Monnet - Case Study - GRE
#For python 3.x

#!/usr/bin/python

import sys
import os
import errno
import json


def list_files(Curpath):
    files = {}
    for file in os.listdir(Curpath):
        file = os.path.join(Curpath, file)
        #Check in Current directory for file and add to the dictionary Files
        if os.path.isfile(file):
            files[file] = os.lstat(file).st_size
    print ("\nList of files in: " + Curpath)
    #Display with order, uncomment next line to sort the files by size.
    #files = sorted(files.iteritems(), key = lambda k:k[1], reverse = True)
    print (json.dumps({"files":files}, indent=6))

def check_subDir(Curpath):
    Dirs = {}
    for Dir in os.listdir(Curpath):
        Dir = os.path.join(Curpath, Dir)
        #Check in Current directory for directory and add to the dictionary Dirs
        if os.path.isdir(Dir):
            Dirs[Dir]= Dir
    if not Dirs:
        sys.exit(1)
    print ("\n***********************************************************************************")
    print ("***********************************************************************************\n")
    question = input("Do you want to see the files in the sub-directory(ies)? Enter Yes or No\n")
    if (question == "Yes" or question == "yes" or question == "y"):
        for Dir in Dirs:
            Error_handling(Dir)
            list_files(Dir)


def Error_handling(mountpoint):
    try:
        #Using Change Directory command to check mountpoint right and access.
        os.chdir(mountpoint)
    except OSError as err:
        # Display Error Message if access required
        if err.errno == errno.EACCES:
            print ("\nSorry! You do not have access to " + mountpoint + " directory! Check with your Admin!\n")
            sys.exit(1)
        # Display Error Message if Mount point does not exist
        if err.errno == errno.ENOENT:
            print ("\nOops! This mountpoint " + mountpoint + " does not exist! Try again!\n")
            sys.exit(1)
        # Display Error Message if not a valid Directory
        if err.errno == errno.ENOTDIR:
            print ("\nOops! This program require a valide directory." + mountpoint + " is not a directory!\n")
            sys.exit(1)


# Length of Arguments required sys.argv[0] and sys.argv[1] exactly two arguments.
if len(sys.argv) != 2:
    print ("\nThis program required one Mount point or Directory: Example " + sys.argv[0] + " /DirectoryName\n")
    sys.exit(1)

mountpoint = sys.argv[1]

print ("\n##########################-Welcome to Get Disk Usage-###########################")

Error_handling(mountpoint)

Curpath = os.getcwd()

list_files(Curpath)

check_subDir(Curpath)

print ("########################-Thank you for using this program-########################")


