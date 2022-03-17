#Program will count word 'the' in the 2 books.
def read_book(book):
    try:
        with open(book) as fb:
            content = fb.read()
    except FileNotFoundError:
        print("Book doesn't exist!")
    else:
        num_the = content.lower().count('the')
        print(f"In the boook {book} the word 'the' appears {num_the} times.")
    
    
books = ['Birds in town.txt','handbook of the trees.txt']
for book in books:
    read_book(book)