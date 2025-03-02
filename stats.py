def count_words (book_text):
  words = book_text.split()

  return len(words)

def count_characters (book_text):
  charDict = {}

  for char in book_text:
    char_to_lowercase = char.lower()

    if (char_to_lowercase in charDict):
      charDict[char_to_lowercase] = charDict[char_to_lowercase] + 1
    else:
      charDict[char_to_lowercase] = 1
  
  return charDict

def sorted_character_count (num_characters):
  for w in sorted(num_characters, key=num_characters.get, reverse=True):
    if (w.isalpha()):
      print(f"{w}: {num_characters[w]}")

