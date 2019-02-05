#!/usr/bin/env python3

# Lab 1 - ME 599 - Johnny Vang
# Given some words, count how many of a certain letter there is
# Example: letter_count(apple,a) = 1


def letter_count(words, letter):
    if type(words) != str or type(letter) != str:
        raise TypeError('Arguments must be a string')
    if len(letter) > 1:
        raise ValueError('Letter should be singular')
    x = 0
    word_list = list(words.lower())
    for i in range(len(word_list)):
        if word_list[i] == letter.lower():
            x += 1
    return x


if __name__ == '__main__':
    # print(letter_count('ABCDDDDD', 'A'))
    # letter_count('b', 'a')
    print(letter_count("a and the threeea aaAAAa", 'a'))

    # this does not work because word_list is not a range?
    # they are saying the list must be integer or slices, not str
    # for i in word_list:
    #     # they are saying the list must be integer or slices, not str
    #     if word_list[i] == letter.lower():
    #         x = x + 1
    # return x
