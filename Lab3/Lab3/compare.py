#!/usr/bin/env python3

import sys
import string
import os.path
from os import path
import errno


def word_counter(filename):
    if type(filename) != str:
        raise ValueError('Argument must be a string file')
    num_words = 0
    combo_break = []
    translator = str.maketrans(string.punctuation, ' ' * len(string.punctuation))  # map punctuation to space
    with open(filename, 'r') as f:
        for line in f:
            words = line.translate(translator).split()
            num_words += len(words)
            for i in words:
                combo_break.append(i.lower())
    print(filename + ":")
    print(" {} words".format(num_words))
    print(" unique: {}".format(len(set(combo_break))))
    return set(combo_break)


def combo(first_txt, second_txt):
    total_words = word_counter(first_txt)
    total_words2 = word_counter(second_txt)
    print("Only {}: {}".format(first_txt, len(total_words.difference(total_words2))))
    print("Only {}: {}".format(second_txt, len(total_words2.difference(total_words))))
    print("Both files: {}".format(len(total_words.intersection(total_words2))))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError('Only 2 command-line arguments allowed. Try Again.')
    else:
        if path.exists(sys.argv[1]) != True:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), sys.argv[1])
        if path.exists(sys.argv[2]) != True:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), sys.argv[2])
    combo(sys.argv[1], sys.argv[2])
