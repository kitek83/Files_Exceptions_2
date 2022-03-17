def read_books(filename):
    try:
        with open(filename) as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Book {filename} doesn't exist!")
    else:
        words = content.split()
        num_words = len(words)
        print(f'The book {filename} has {num_words} words.')

books = ['alice.txt','little_women.txt','siddhartha.txt','moby_dick.txt']
for book in books:
    read_books(book)
