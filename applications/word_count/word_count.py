import re

def word_count(s):
    # initialize cache
    cache = {}
    # if s is an empty string return empty dic
    if s == "":
        return cache
    # set string to lower case
    string = s.lower()
    # initialize list of forbidden characters
    forbidden_char = ["\"", "\\", ":", ";", ",", ".", "-", "+", "=", "/", "|", "[", "]", "{", "}", "(", ")",  "*", "^", "&"]
    # initialize list of white spaces that aren't space
    alt_white_space = ["\n", "\r", "\t"]
    # replace all forbidden characters with empty strings
    for char in forbidden_char:
        string = string.replace(char, "")
    # replace all white spaces not spaces with a space
    for space in alt_white_space:
        string = string.replace(space, " ")
    # create list of strings split by spaces
    words = string.split(" ")
    # iterate through list
    for word in words:
        # ensure item is not empty string
        if word != "":
            # if word is already in cache, +1 to value
            if word in cache:
                cache[word] += 1
            # if word not in cache, set word to key and 1 to value
            else:
                cache[word] = 1
    # print/return cache
    print(cache)
    return cache



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))