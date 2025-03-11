filepath = str()

def get_book_text(filepath):
    with open(filepath) as f:
        book_string = f.read()

    return book_string

def main():
    filepath = "~/progetti/BookBot/books/frankenstein.txt"


main()
