#!/usr/bin/env python3
# HW05_ex09_01.py

# Write a program that reads words.txt and prints only the
# words with more than 20 characters (not counting whitespace).
##############################################################################
# Imports

# Body
def readwords():
    fin = open('words.txt', 'r')
    line = fin.readline()

    for line in fin:
        if len(line) >= 20:
            print(line)


##############################################################################
def main():
    readwords()
    pass  # Call your functions here.

if __name__ == '__main__':
    main()
