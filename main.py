from stats import get_number_of_words, get_number_of_characters, get_sorted_characters, get_words_with_numbers
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
    words = get_words_with_numbers(book_text)
    sorted_words = get_sorted_characters(words)
    top_10_words = list(sorted_words.items())[:10]


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("----------- Top 10 Words ----------")
    for word, value in top_10_words:
        print(f"{word}: {value}")
    print("--------- Character Count -------")
    for character in sorted_characters:
        if character.isalpha() == True:
            print(f"{character}: {sorted_characters[character]}")
    print("============= END ===============")

    

main()
