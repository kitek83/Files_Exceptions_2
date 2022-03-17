file = 'alice.txt'
try:
    with open(file) as f:

        content = f.read()
except FileNotFoundError:
    print(f'File {file} does not exist!')
else:
    print(content)
