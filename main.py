def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    split_words = text.split()
    num_words = 0
    for word in split_words:
        num_words += 1
    print(f"{num_words} words found in the document")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()