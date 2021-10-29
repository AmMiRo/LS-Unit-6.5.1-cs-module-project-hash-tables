# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
# Read in all the words in one go
with open("ciphertext.txt", encoding="utf-8") as f:
    text = f.read()
# list of most to least commonly used letters in the english alphabet
frequency_lst = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L", "W", "U", "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z"]
# initialize dic where letter is key and number of uses is value
letter_frequency = {}
# initialize dic where 
key = {}
# iterate through text
for char in text:
    # ensure character is letter
    if char.isalpha():
        # if char already in letter_frequency +1 to value
        if char in letter_frequency:
            letter_frequency[char] += 1
        # if char not in letter_frequency set value to 1
        else:
            letter_frequency[char] = 1
# create list of tuples of letter_frequency entries
tuple_lst = list(letter_frequency.items())
# sort list from most to least used characters
tuple_lst.sort(key=lambda tup: tup[1], reverse=True)
# for letter in frequency list populate key with tuple character for key and letter for value
for i in range(len(frequency_lst)):
    key[tuple_lst[i][0]] = frequency_lst[i]
# initialize new string
new_str = ""
# iterate through text
for char in text:
    # if character is letter add value from key to string
    if char.isalpha():
        new_str += key[char]
    # if character is not letter add character to string
    else:
        new_str += char

# print new string
print(new_str)
