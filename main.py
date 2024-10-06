def main():
    book_path = "books/frankenstein.txt"
    book_text = get_text(book_path)
    book_count = get_count(book_text)
    char_count = get_char_count(book_text)
    organize(book_path, book_count, char_count)

def get_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()
    
def get_count(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {}
    for char in text:
        lower_char = char.lower()
        if lower_char in char_dict.keys():
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1
    return char_dict

def organize(book_path, word_count, char_dict):
    print(f"--- Begin Report on {book_path} ---")
    print("")
    print(f"{word_count} words found in the document")
    print("")

    sorted_list = sorted(char_dict.items(), key = lambda x: x[1], reverse = True)
    for pair in sorted_list:
        if pair[0].isalpha():
            print(f"The {pair[0]} character was found {pair[1]} times")
            
    print("")
    print("--- End Report ---")

main()