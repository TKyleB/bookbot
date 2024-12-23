
def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_dict = get_character_count(book_text)
    print_report(book_path, num_words, char_dict)

def count_words(text: str):
    return len(text.split())

def get_book_text(file_path: str):
    with open(file_path) as f:
        return f.read()
    
def get_character_count(text: str):
    characters = {}
    for c in text.lower():
        if c.isalpha():
            if c in characters:
                characters[c] += 1
            else:
                characters[c] = 1
    # Returns sorted dict from largest to smallest
    return {k: v for k, v in sorted(characters.items(), key=lambda item: item[1], reverse=True)}

def print_report(book_path, num_words, char_dict):
    print(f"--- Begin Report for {book_path} ---")
    print(f"{num_words} found in the document")
    for key in char_dict:
        print(f"The letter {key} was found {char_dict[key]} times")
    print("--- End Report ---")
    

main()