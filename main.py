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
    
    # After getting your sorted character list and word count
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    # Loop through your sorted character list
    for char_dict in list_output:
        char = char_dict["char"]
        count = char_dict["num"]
    
    # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


main("books/frankenstein.txt")