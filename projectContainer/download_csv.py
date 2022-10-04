#!/usr/bin/env python

from datasets import load_dataset


def process_file(text_file):
    """
    Opens, reads, and closes a given file.
    Returns the contents of this file as a string.
    """
    with open(text_file, encoding="utf-8") as file:
        data_path = file.read()

    return data_path

data = process_file('data.txt')
print(data)


#dataset = load_dataset('squad', split='train')