#books = ['alice.txt','little_women.txt','moby_dick.txt','siddhartha.txt']: files downloaded from: https://www.gutenberg.org/
#Counting number of words in 4 different books...
title = 'Alice in Wonderland'
print(len(title))
print('Using split() function:')
print(title.split())
new_title = title.split()
print(new_title)
print(len(new_title))
print(3*'-------------------')
print()

def count_words(file_text):
    try:
        with open(file_text) as f:
            content = f.read()
    except FileNotFoundError:
        pass
    try:
        book = content.split()  #creating the list of words from the books
        number_words = len(book)
        print(f'The file {file_text} has {number_words} words.')
    except UnboundLocalError:
        pass

file = 'alice.txt'
count_words(file)
print(3*'===============================')
print()

print('Counting number of words in 4 different books...')
books = ['alice.txt','little_women.txt','moby_dick.txt','siddhartha.txt']
#file moby_dick.txt doesn't exist
#using the function count_word() with the loop
for boo_k in books:
    count_words(boo_k)



