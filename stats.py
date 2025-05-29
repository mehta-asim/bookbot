def  get_number_of_words(book_text):
    number_of_words = len(book_text.split())
    return number_of_words
    

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
