#Write a while loop thet prompts user for their name. When their enter their name,
#print the greeting to the screen and add a line recording their visit in file
#called guest_book.txt. Make sure each entry appears on a new line in the file.

file = 'guest_book.txt'
count = 0
while True:
    name = input('Please enter Your name and surname: ')
    print(f'Hello {name}!')
    with open(file, 'a') as file_ob:
        count += 1
        file_ob.write(f'Visitor nr.{count}. Name:{name}.\n')
        quit = input('Enter q to quit or enter to continue.')
        if quit == 'q':
            break

        