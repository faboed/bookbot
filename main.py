from stats import count_words, count_chars, count_chars_list

# Calls a function to import text from a filepath and transforms it into a book report based on functions in stats.py
def main(path):
    with open(path) as f:
        book_text = f.read()
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