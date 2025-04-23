def main():
    print(get_book_text("books/frankenstein.txt"))

def get_book_text(filepath):
    with open(filepath, encoding="utf8") as f:
        file_content = f.read()
    return file_content

main()