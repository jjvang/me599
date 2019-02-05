#!/usr/bin/env python3


def apply_null_filter(data):
    """
    Apply the null filter to an iterable, returning a list.
    """

    # Make an empty list
    filtered = []

    # Add one element at a time to the list.  There are a lot of ways to do this; this is just one of them.
    for datum in data:
        filtered.append(datum)

    # Return the new list
    return filtered


if __name__ == '__main__':
    # Check to see if it equal itself? why wouldn't it?
    # filter just goes and makes it a list again, maybe to check if after some fake data it matches?
    # Generate a list of numbers
    data = [1,2,3,4,5]
    print(data)

    # Run the null filter over the data
    filtered = apply_null_filter(data)
    print(filtered)

    # Check that the filter didn't do anything
    for d,f in zip(data, filtered):
        if d != f:
            print('Found a mismatch.  Null filter failed')

    print('Testing finished')