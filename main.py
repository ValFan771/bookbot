from stats import *
import sys

def main():
    with open(sys.argv[1], encoding="UTF-8") as f:
        file_content = f.read()
    words_count = get_words_count(file_content)
    char_count = get_char_count(file_content)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for entry in sort_dict(char_count):
        if entry[0].isalpha():
            key, value = entry[0], entry[1]
            print(f"{key}: {value}")
    print("============= END ===============")

if len(sys.argv) == 2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)