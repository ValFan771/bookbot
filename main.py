from stats import get_words_count

def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
    words_count = get_words_count(file_content)
    print(f"{words_count} words found in the document")

main()