#Handling the exceptions...
try:
    print(5/0)
except ZeroDivisionError:
    print('You can not divide by 0.')
print(3*'----------------------')
print()

print('Give me 2 numbers and I will divide them...')
print("Enter 'q' to quit.")
while True:
    first_number = input('Enter the 1st number: ')
    if first_number == 'q':
        break
    second_number = input('Enter 2nd number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)