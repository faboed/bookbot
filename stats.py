# turning the string into a list with .split() and counting the words with a loop
def count_words(book_text):
    word_count = 0
    book_text_list = book_text.split()
    for word in book_text_list:
        word_count += 1
    return word_count

#counts the unique characters, numbers and special character in the input text and returns it as a dict
def count_chars(book_text):
    char_count = {}
    for char in book_text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

#sorting function
def sort_on(dict):
    return dict["num"]

#turns the dictionary into a list of dictionaries for a pretty print and sorts it
def count_chars_list(char_count):
    list_char_count = []
    for k, v in char_count.items():
        list_char_count.append({"char": k, "num": v})
    list_char_count.sort(reverse=True, key=sort_on)
    return list_char_count
