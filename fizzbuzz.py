"""
Write a program that prints the numbers from 1 to n. But for multiples of 3,
print "Fizz" instead of the number, and for the multiples of 5, print "Buzz."
For numbers that are multiples of both 3 and 5, print "FizzBuzz."
"""

def fizzbuzz(n):
    for i in range(1, n):
        if (i % 3 == 0) and (i % 5 == 0):
            print('FizzBuzz')
            continue
        if i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)
