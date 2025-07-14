#!/usr/bin/env python3
import sys
char = sys.argv[2]
input_file = sys.argv[1]
print("input character is: ", char)

#open a file and insert new character for each line
def insert_char_in_file(input_file, char):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    with open(input_file, 'w') as file:
        for line in lines:
            file.write(char + line)
    return

insert_char_in_file(input_file, char)
