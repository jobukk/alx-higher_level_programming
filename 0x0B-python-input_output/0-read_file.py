#!/usr/bin/python3
"""Read file Modele"""


def read_file(filename=""):
    """Fucn to read file"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
