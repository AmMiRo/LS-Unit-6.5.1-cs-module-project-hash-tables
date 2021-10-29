import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# initialize dictionary of words
words_dic = {}
# replace all new line characters with spaces
new_line = "\n"
words = words.replace(new_line, " ")
# create list splitting words at spaces
words_lst = words.split(" ")
# iterate through words_list
for i in range(len(words_lst) - 1):
    # if the word is in dictionary and not already in value, add to value
    if words_lst[i] in words_dic:
        if words_lst[i + 1] not in words_dic[words_lst[i]]:
            words_dic[words_lst[i]] += [words_lst[i + 1]]
    # if word not in dictionary add word as key and next word as value
    else:
        words_dic[words_lst[i]] = [words_lst[i + 1]]

# TODO: construct 5 random sentences
# repeat process 5 times
for i in range(5):
    # initialize random word as first word
    word = random.choice(list(words_dic))
    # initialize string with first word
    string = word
    # repeat process randome number between 15 and 20 times
    for j in range(random.randrange(15, 20)):
        # if only 1 next word set that as new_word
        if len(words_dic[word]) == 1:
            new_word = words_dic[word][0]
        # if > 1 next words set random next word as new_word
        else:
            new_word = words_dic[word][random.randrange(0, len(words_dic[word]) - 1)]
        # add new_word to string with space
        string += " " + new_word
        # set word to new_word
        word = new_word
    # print sentence with first letter capitalized and period at end
    print(string[0].capitalize() + string[1:] + ".")
