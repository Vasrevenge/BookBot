import os
import sys
from stats import count_words,count_characters,dictionary_presentation
file_path = str()

def main():

    if len(sys.argv) < 2:
        print("Usage : python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]                     #r"/home/jack/progetti/BookBot/books/frankenstein.txt"
    content = get_book_text(file_path)
    word_number = count_words(content)

    c_dict = count_characters(content)
    c_set = dictionary_presentation(c_dict)
    new_list = list() 
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at :", file_path)
    print("----------- Word Count ----------")
    print('Found',word_number,'total words')
    print("--------- Character Count -------")
    for d in c_set:
        a = str(d[0])
        if a.isalpha():
            print( d[0]+":", d[1])            

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

main()
