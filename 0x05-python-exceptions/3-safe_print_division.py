#!/usr/bin/python3
def safe_print_division(a, b):
    """safe print the division using execption"""
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
    finally:
        print("Inside result: {}".format(div))
        return div
