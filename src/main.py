#!/usr/local/bin/python3
# -*- coding: utf-8 -*- c

import os
import sys
import interpreter 

def main():
    
    content  = ""           # This variable will hold the contents of the source code
    path     = os.getcwd()  # Holds path this script was executed from

    # Holds the name of the file the user wants to compile
    try: fileName = sys.argv[1]
    except:
        print("[ERROR] Expected 1 Argument Containing File Name to be Run e.g 'minverva main.mnv'")
        return

    # Check if the file extension is correct
    if fileName[len(fileName) - 4:len(fileName)] != ".mnv":
        print("[ERROR] File extension not recognised please make sure extension is '.mnv'")
        return # quit programme

    # Check to make sure that only one argument is passed
    try:
        print('[ERROR] Expected 1 argument found 2 (' + sys.argv[1] + ", " + sys.argv[2] + ')')
        return # quit programme
    except: pass

    try:
        # Open source code file and get it's content and save it to the 'contents' var
        with open(path + "/" + fileName, "r") as file:
            new_file = interpreter.Dragoon()
            new_file.parse(file)
    except FileNotFoundError:
        print("[FileError] Cannot find {}".format(fileName))
    

main()
