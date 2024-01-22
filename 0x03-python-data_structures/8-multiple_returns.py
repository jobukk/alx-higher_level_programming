#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0
    if sentence == "":
        first_char = None
        return length, first_char
    for char in sentence:
        length += 1
    first_char = sentence[0]
    return length, first_char
