import sys

def count_words(book_text):
    word_count = 0
    book_text_list = book_text.split()
    for word in book_text_list:
        word_count += 1
    return word_count

def count_chars(book_text):
    char_count = {}
    for char in book_text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def count_chars_list(char_count):
    list_char_count = []
    for k, v in char_count.items():
        list_char_count.append({"char": k, "num": v})
    list_char_count.sort(reverse=True, key=sort_on)
    return list_char_count

def report(path):
    with open(path) as f:
        book_text = f.read()
    
    word_count = count_words(book_text)
    char_count = count_chars(book_text)
    list_output = count_chars_list(char_count)
    
    # Return data for GUI instead of printing
    return {
        "word_count": word_count,
        "character_data": list_output
    }