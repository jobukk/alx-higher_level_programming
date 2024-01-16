#!/usr/bin/python3
def fizzbuzz():
    #3 mutiples-Fizz
    #5 multiples - Buzz
    #3 and 5 multiples -FizzBuzz
    for x in range(1,101):
        if x % 3 == 0:
            print("Fizz ", end=" ")
        elif x % 5 == 0:
            print("Buzz ", end=" ")
        elif x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz ", end=" ")
        else:
            print(x, end=" ")
