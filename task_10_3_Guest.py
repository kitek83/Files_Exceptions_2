#Write the program that prompts the user for their name.
#When the respond, write their name to a file called guest.txt
file = 'guest.txt'

while True:
    name = input('Please enter your name and surname: ')
    with open(file, 'a') as file_ob:
        file_ob.write(name+'\n')
    quit = input('Enter q to quit or enter to continue: ')
    if quit == 'q':
        break
