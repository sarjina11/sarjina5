#!/usr/bin/env python3
# Author ID: skarki28

def read_file_string(file_name):
    """
    Reads the entire contents of the file as a single string.
    """
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    """
    Reads the file contents and returns a list of lines without newline characters.
    """
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))

