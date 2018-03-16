#!/usr/bin/env python
"""\
fileEditor.py

A file editor that can create files and can edit the desired file.
File path is fixed however
usage: fileEditor.py
"""
import sys
import pickle
import os

# flag for continuous input
menu = 1

# if called incorrectly exit the program
if len(sys.argv[1:]) != 0:
  sys.exit(__doc__)

fileName = input("Put the name of the file: ")

# store filepath in string
filepath = "data/" + fileName + ".pk1"

def printfile():
    for x in output:
        print(x + "\r\n")
    return

def append():
    global output
    entering = 1
    while (entering):
        buffer = input("Put contents of the file ({STOP} to exit): ")
        if '{STOP}' in buffer:
            entering = 0
        else:
            output.append(buffer)
    return


def delete():
    global output
    entering = 1
    counter = 0
    while (entering):
        buffer = input("Delete contents of the file ({STOP} to exit): ")
        if '{STOP}' in buffer:
            entering = 0
        else:
            for x in output:
                counter += 1
                if buffer in x:
                    output.remove(x)
                    print(x + " was removed.")
                    break
            if counter == len(output):
                print(buffer + " was not found")
    return

# if the file does not exist already create one, otherwise append
if not os.path.isfile(filepath):
    output = []
else:
    with open(filepath, "rb") as write_file:
        output = pickle.load(write_file)

# menu for options
while (menu):
    print("[0] Print contents of file\r\n[1] Input into file\r\n[2] Delete from file\r\n[3] Exit and Save")
    choice = input("_: ")
    if "0" in choice:
        printfile()
    elif "1" in choice:
        append()
    elif "2" in choice:
        delete()
    elif "3" in choice:
        menu = 0


with open(filepath, "wb") as write_file:
    pickle.dump(output, write_file)
