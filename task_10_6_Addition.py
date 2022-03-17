#If you enter text, ValueError appears.
try:
    num1 = input('Enter nr1: ')
    num2 = input('Enter nr2: ')
    result = int(num1) + int(num2)
except ValueError:
    print('You must enter only numbers.')
else:
    print(f'Result = {result}')

