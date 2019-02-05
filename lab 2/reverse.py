#!/usr/bin/env python3

# ME 599 - Johnny Vang - Lab 2
# This function outputs the reverse of the arguments
# Example:
# reverse_i('hello') == reverse_r('hello') -> ['o', 'l', 'l', 'e', 'h']
# reverse_i([1, 2, 3, 4, 5]) == reverse_r([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]


def reverse_r(your_list):
    new = []
    # For Number arguments
    # Ex: 1,[1],[1, 2, 3, 4, 5]
    if type(your_list) == int or len(your_list) == 1:
        return your_list
    if type(your_list[0]) == int:
        new = [your_list[-1]] + reverse_r(your_list[:-1])
    # Accepts a single string and list with string variables:
    # Ex: "hello", ['a', 'b', 'c'], ['a']
    if len(your_list) > 1 and type(your_list[0]) == str:
        if type(your_list) == str:
            your_list = list(your_list)
        new = [your_list[-1]] + reverse_r(your_list[:-1])
    return new


def reverse_i(your_list):
    new = []
    # For Number arguments
    # Ex: 1,[1],[1, 2, 3, 4, 5]
    if type(your_list) == int or len(your_list) == 1:
        return your_list
    if type(your_list[0]) == int:
        for x in your_list:
            new.append(your_list[-x])
    # Accepts a single string and list with string variables:
    # Ex: "hello", ['a', 'b', 'c'], ['a']
    if len(your_list) > 1 and type(your_list[0]) == str:
        if type(your_list) == str:
            your_list = list(your_list)
        for x in range(len(your_list)):
            new.append(your_list[-1 - x])  # Need -1 because x starts at 0 for a string list (for range?)
    return new


if __name__ == '__main__':
    # Test Test
    if reverse_r('hello') == reverse_i('hello'):
        print('reverse_r(''hello'') = reverse_i(''hello'')')
    if reverse_r([1, 2, 3, 4, 5]) == reverse_i([1, 2, 3, 4, 5]):
        print('reverse_r(''[1, 2, 3, 4, 5]'') = reverse_i(''[1, 2, 3, 4, 5]'')')

    # Test for recursive
    letter2 = reverse_r(['a', 'b', 'c', 'd'])
    word2 = reverse_r("hello")
    single2 = reverse_r("h")
    single_list_letter2 = reverse_r(['h'])
    # print(letter2, word2, single2, single_list_letter2)
    number2 = reverse_r([1, 2, 3, 4, 5])
    single_number2 = reverse_r(1)
    single_list_number2 = reverse_r([1])
    # print(number2, single_number2, single_list_number2)

    # Test for iterative
    letter = reverse_i(['a', 'b', 'c', 'd'])
    word = reverse_i("hello")
    single = reverse_i("h")
    single_list_letter = reverse_i(['h'])
    # print(letter, word, single, single_list_letter)
    number = reverse_i([1, 2, 3, 4, 5])
    single_number = reverse_i(1)
    single_list_number = reverse_i([1])
    # print(number, single_number, single_list_number)

    # Test Word Arguments
    if letter == letter2 and word == word2 and single == single2 and single_list_letter == single_list_letter2:
        print("PASS, all letter arguments match")
    if number == number2 and single_number == single_number2 and single_list_number == single_list_number2:
        print("PASS, all number arguments match")
