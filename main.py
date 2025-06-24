import sys
from stats import get_num_words, get_num_char, dict_sort


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_num_char(text)
    final_dict = dict_sort(char_count)
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {book_path}...")
    print("--------- Word Count ---------")
    print(f"Found {num_words} total words")
    print("------- Character Count -------")
    for c in final_dict:
        print(f"{c}: {final_dict[c]}")
    print("=========== END ===========")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
