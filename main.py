from stats import count_words, count_characters, sorted_character_count
import sys

def get_book_text (path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
  
  return file_contents

def main ():
  if (len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    book_text = get_book_text(sys.argv[1])

    num_words = count_words(book_text)
    num_characters = count_characters(book_text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_character_count(num_characters)
    print("============= END ===============")

main()