while True:
    try:
        num1 = input('Enter nr1: ')
        num2 = input('Enter nr2: ')
        sum = int(num1) + int(num2)
    except ValueError:
        pass
    else:
        print(f'num1+num2 = result = {sum}')
    quit = input('Enter q to quit or enter to conrinue.')
    if quit == 'q':
        break

