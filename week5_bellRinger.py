# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
magic = "abracadabra"
# a. Retrieve the 5th character.
print(magic[4])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.find("c"))

# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
alphabet = "abcdefghijklmnopqrstuvwxyz"
# a. Extract the letters 'hij' #hij_index = alphabet.index('hij')
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
extracted_letters = alphabet[1::2]
print(extracted_letters)
# c. Reverse the entire string using slicing.
reversed_string = alphabet[::-1]
print(reversed_string)
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote[-16: ])

info = "Python is fun. Fun is good. Good is subjective."
start_index = info.find('subjective')
if start_index != -1:
    end_index = start_index + len('subjective')
    word = info[start_index:end_index]
    print(word)
# b. Extract every third word.
words_list = info.split()
third_words = words_list[2::3]
print(f"Original sentence: {info}")
print(f"List of words: {words_list}")
print(f"Every third word: {third_words}")
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
reversed_string = words_list[::-1]
# Problem Set 3: String Methods
# Upper & Lower:
print("Uppercase:", info.upper()) 
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
print("Lowercase:", info.lower())
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
motto = "[Make", "haste", "slowly.]"
# a. Convert the list into a single string.

# b. Now, split the string at every occurrence of the letter 'a'.
reversed_word_positions = info.split()[::-1]
reversed_word_positions = ' '.join(reversed_word_positions)
print(reversed_word_positions)
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
# b. Replace "plans" with "mistakes".
phrase2 = "life is what happens when you are busy making other plans"
new_phrase = phrase2.replace("busy", "distracted")
new_phrase2 = phrase2.replace("plans", "mistakes")
print(new_phrase)
print(new_phrase2)
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7
word = 'iteration'
repeated_word = word * 7
print(repeated_word)
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
text = "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
word_to_find = "moonlight"

if target_word.lower() in quote.lower():
    print(f'The word "{target_word}" appears in the quote.')
else:
    print(f'The word "{target_word}" does not appear in the quote.')
# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.