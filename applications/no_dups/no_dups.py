def no_dups(s):
    # initialize cache
    cache = {}
    # create list of words split at space
    words = s.split(" ")
    # initialize non_dups list
    non_dups = []
    # iterate through words
    for word in words:
        # if word is not in cache add it to cache and non_dup list
        if word not in cache:
            cache[word] = True
            non_dups.append(word)
    # solution is string of non_dups words joined by spaces
    solution = " ".join(non_dups)
    # return solution
    return solution




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))