#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
num = str(number)
last_digit = num[-1]
if int(last_digit) > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == '0':
    print(f"Last digit of {number} is {last_digit} and is 0")
elif 0 < int(last_digit) < 6:
    print(f"Last digit of {number} is -{last_digit} and is less than 6 and not 0")