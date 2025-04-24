from stats import *

def main():
    with open("books/frankenstein.txt", encoding="UTF-8") as f:
        file_content = f.read()
    words_count = get_words_count(file_content)
    char_count = get_char_count(file_content)
    print(f"{words_count} words found in the document")
    print(char_count)

main()