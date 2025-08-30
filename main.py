from stats import calculate_num_of_words, calculate_num_of_characters, sort_characters
import sys

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content


def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    content = get_book_text(book_path)
    num_of_words = calculate_num_of_words(content)
    chars = calculate_num_of_characters(content)
    chars_sorted = sort_characters(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for char in chars_sorted:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    
    print("============= END ===============")


    

main()
    