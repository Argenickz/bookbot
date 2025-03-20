from stats import *
import sys


def get_book_text(filepath):
    with open(filepath) as file:
        book = file.read()
        return book

if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)


filepath = sys.argv[1]

# Try/except in case of a typo or invalid filepath
try:
    text = get_book_text(filepath)
    def main():
        num_words = get_num_words(text)
        character_count = count_characters(text)
        sorted_list_of_dicts = create_functional_dictionaries(character_count)
        print_report(sorted_list_of_dicts, filepath, num_words)
    main()
except Exception:
    print('No such file or directory, please verify the filepath')










