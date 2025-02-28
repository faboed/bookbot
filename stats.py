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
    char_list = []
    for char in book_text:
        if char not in char_list:
            char_list.append(char.lower())
    for char in char_list:
        char_counter = 0
        if char in book_text.lower():
            char_counter += 1
        char_count[char] = char_counter
    # print(char_list)
    # print(char_count)
    return char_count

# count_chars("ABCDE")