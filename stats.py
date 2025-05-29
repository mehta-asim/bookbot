def  get_number_of_words(book_text):
    number_of_words = len(book_text.split())
    return number_of_words

def get_words_with_numbers(book_text):
    word_with_numbers = {}
    words = book_text.split()
    for word in words:
        word = word.lower()
        if word in word_with_numbers:
            word_with_numbers[word] += 1
        else:
            word_with_numbers[word] = 1
    
    return word_with_numbers


def get_number_of_characters(book_text):
    characters = {}
    for text in book_text:
        chars = list(text)
        for char in chars:
            char = char.lower()
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def get_sorted_characters(characters):
    items = list(characters.items())
    items.sort(key=lambda item: item[1], reverse=True)
    sorted_dictionary = dict(items)
    return sorted_dictionary
