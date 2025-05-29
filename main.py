from stats import get_number_of_words, get_number_of_characters, get_sorted_characters
import sys

def get_book_text(filepath): 
    with open(filepath) as f:
        return f.read()

def main():
    # filepath = '/books/frankenstein.txt'
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text('./' + filepath)
    number_of_words = get_number_of_words(book_text)
    number_of_characters = get_number_of_characters(book_text)
    sorted_characters = get_sorted_characters(number_of_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for character in sorted_characters:
        if character.isalpha() == True:
            print(f"{character}: {sorted_characters[character]}")
    print("============= END ===============")

    

main()
