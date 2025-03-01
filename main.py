from stats import count_words
from stats import count_chars
from stats import count_chars_list
# calling the filepath of a specific book with get_book_text()
#f.read is turning inputs into strings
def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

# prints the relative path to a specific book calling the function
def main(path):
    book_text = get_book_text(path)
    word_count = count_words(book_text)
    char_count = count_chars(book_text)
    list_output = count_chars_list(char_count)
    print(f"{word_count} words found in the document")
    #print(char_count)
    print(list_output)

main("books/frankenstein.txt")