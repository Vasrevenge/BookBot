import os
from stats import count_words,count_characters
file_path = str()
# r"/home/jack/progetti/BookBot/books/frankenstein.txt"

def main():
    file_path = r"/home/jack/progetti/BookBot/books/frankenstein.txt"
    content = get_book_text(file_path)
    word_number = count_words(content)

    c_set = count_characters(content)

    print(word_number,"words found in the document")
    print(c_set)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

main()
