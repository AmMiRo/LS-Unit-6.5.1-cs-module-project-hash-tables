# Your code here
# Read in all the words in one go
with open("robin.txt") as f:
    words = f.read()

# initialize length of longest word
length = 0
# dic of word as key and number of occurrences as value
words_dic = {}
# list of forbidden characters
forbidden_char = ["\"", "\\", ":", ";", ",", ".", "-", "+", "=", "/", "|", "[", "]", "{", "}", "(", ")",  "*", "^", "&"]
# for each forbidden character replace character with empty string
for char in forbidden_char:
    words = words.replace(char, "")
# replace line breaks with spaces
words = words.replace("\n", " ")
# create list of words from words
words_arr = words.split(" ")

for word in words_arr:
    # make word lower case
    word = word.lower()
    # ensure it is not an empty string
    if len(word) > 1:
        # if length of word is greater than length set word length as length
        if len(word) > length:
            length = len(word)
        # if word in words_dic subtract 1 from value
        if word in words_dic:
            words_dic[word] -= 1
        # if word isn't in words_dic set word to key with -1 as value
        else:
            words_dic[word] = -1
# create list of key, value pairs as tuples
tuple_lst = list(words_dic.items())
# sort tuple_arr first by value then by key
tuple_lst.sort(key=lambda tuple: (tuple[1], tuple[0]))
# initialize solution string
solution = ""
# for tuple in list add key lt justified to length of longest word +1 followed by hashes for the absolute value followed by line break
for tup in tuple_lst:
    solution += tup[0].ljust(length + 1) + "#" * abs(tup[1]) + "\n"

# return solution
print(solution)