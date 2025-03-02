from stats import count_words, count_characters

def get_book_text (path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
  
  return file_contents

def main ():
  book_text = get_book_text("./books/frankenstein.txt")

  num_words = count_words(book_text)
  num_characters = count_characters(book_text)

  print(f"{num_words} words found in the document")
  print(num_characters)

main()