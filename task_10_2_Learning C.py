#Opening the txt file and replacing the word Python with Anaconda
file = 'learning_python.txt'
with open(file) as file_ob:
    content = file_ob.read()
    print(content)
print()

print(content.replace('Python','Anaconda'))
print()

with open(file) as file_o:
    lines = file_o.readlines()
for line in lines:

    print(line.replace('Python','Anaconda').rstrip())