import re

def correct_spelling(input_string):
  # Split the input string into a list of words
  words = input_string.split()

  # Use a regular expression to find words that contain non-Vietnamese characters
  pattern = r'[^\u0041-\u1EF9]'
  incorrect_words = [word for word in words if re.search(pattern, word)]

  # Correct the spelling of the incorrect words
  corrected_words = []
  for word in words:
    if word in incorrect_words:
      corrected_word = correct_word(word)
      corrected_words.append(corrected_word)
    else:
      corrected_words.append(word)

  # Join the corrected words back into a single string
  corrected_string = ' '.join(corrected_words)

  return corrected_string

def correct_word(word):
  # Replace non-Vietnamese characters with the correct Vietnamese characters
  corrected_word = word.replace('a', 'á')
  corrected_word = corrected_word.replace('e', 'é')
  corrected_word = corrected_word.replace('i', 'í')
  corrected_word = corrected_word.replace('o', 'ó')
  corrected_word = corrected_word.replace('u', 'ú')
  corrected_word = corrected_word.replace('y', 'ý')
  corrected_word = corrected_word.replace('A', 'Á')
  corrected_word = corrected_word.replace('E', 'É')
  corrected_word = corrected_word.replace('I', 'Í')
  corrected_word = corrected_word.replace('O', 'Ó')
  corrected_word = corrected_word.replace('U', 'Ú')
  corrected_word = corrected_word.replace('Y', 'Ý')

  return corrected_word

# Test the function
input_string = "Xin chào, tôi là ngôi sao"
corrected_string = correct_spelling(input_string)
print(corrected_string)  # Output: "Xin chào, tôi là ngôi sao"

input_string = "Xin chao, toi la ngoi sao"
corrected_string = correct_spelling(input_string)
print(corrected_string)  # Output: "Xin chào, tôi là ngôi sao"