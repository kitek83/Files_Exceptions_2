with open('pi_digits.txt') as file_o:
    content = file_o.read()
    print(content)
print(3*'--------------------------')

file = 'pi_digits.txt'
with open(file) as file_ob:
    for line in file_ob:
        print(line)
print(3*'---------------------------')

file1 = 'pi_digits.txt'
with open(file1) as f_obj:
    lines = f_obj.readlines()
    print(lines)
    for line in lines:
        print(line)
print(3*'======================')

file2 = 'pi_digits.txt'
with open(file2) as file_obj:
    lines = file_obj.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string)
print(f'Length:{len(pi_string)}')
print(3*'~~~~~~~~~~~~~~~~~~~~')

#opening txt file containing 1 000 000 digits.
file = 'pi_million_digits.txt'
with open(file) as file_ob:
    lines = file_ob.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52])
print(f'Length: {len(pi_string)}')

#checking if my birthday appears in the first miliom digits of pi.
birthday = input('Enter your birthday in format: ddmmyy: ')
if birthday in pi_string:
    print('Your birthday appears in first milion digits of pi.')
else:
    print('Your birthday does not apper.')




























