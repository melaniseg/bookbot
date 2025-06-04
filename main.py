from stats import num_of_words
from stats import char_count
from stats import sort_report
import sys

try:
    sys.argv[1]
except IndexError:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]

def get_book_text(book_path):
    with open(book_path) as f:
        book_contents = f.read()
        return book_contents


def main():
    book_text = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(num_of_words(book_text))
    print("--------- Character Count -------")
    sorted_list = sort_report(char_count(book_text))
    num_dict = len(sorted_list)
    for i in range(num_dict):
        letter = sorted_list[i]['char']
        counted = sorted_list[i]['num']
        print(f"{letter}: {counted}")
    print("============= END ===============")


main()

