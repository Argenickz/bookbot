def get_book_text(filepath):
    with open(filepath) as file:
        book = file.read()
        return book
    

filepath = 'books/frankenstein.txt'

print(f"{len(get_book_text(filepath).split())} words found in the document")

def get_num_words():
    pass