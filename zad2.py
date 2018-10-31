"""
Write a Python program that can simulate a simple calculator,
using the console as the exclusive input and output device.
That is, each input to the calculator, be it a number, like 12.34 or 1034,
or an operator, like + or = , can be done on a separate line.
After each such input, you should output to the Python console
what would be displayed on your calculator.
"""

operator = '-'

num = eval(input('Enter number: '))
result = num


while operator != '=':

    operator = input("Would you like to do +, -, *, / or = ? ")

    if operator not in ['+', '-', '*', '/', '=']:
        print('Invalid input!')
        quit()

    else:

        if operator == '+':
            num = eval(input('Enter number: '))
            result += num

        elif operator == '-':
            num = eval(input('Enter number: '))
            result -= num

        elif operator == '*':
            num = eval(input('Enter number: '))
            result *= num

        elif operator == '/':
            num = eval(input('Enter number: '))
            result /= num


print(result)