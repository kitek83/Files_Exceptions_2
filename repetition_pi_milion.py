file = 'pi_million_digits.txt'
with open(file) as file_ob:
    lines = file_ob.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print(pi_string[:52])
print(len(pi_string))
print(len(pi_string[:52]))