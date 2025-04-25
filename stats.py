def get_words_count(file_content):
    words = file_content.split()
    words_count = len(words)
    return words_count

def get_char_count(file_content):
    chars = dict()
    lower_content = file_content.lower()
    for char in lower_content:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_dict(dictionary):
    dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return dictionary