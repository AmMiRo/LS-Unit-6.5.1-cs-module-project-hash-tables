"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
# dic with tuple of inputs from q as key and added value as value
added = {}
# dic with subtracted value as key and tuple of inputs as value
subtracted = {}

# nested for loop to populate added/subtracted
for i in q:
    for j in q:
        plus_val = f(i) + f(j)
        plus_key = (i, j)
        added[plus_key] = plus_val

        sub_key = f(i) - f(j)
        sub_val = (i, j)
        subtracted[sub_key] = sub_val

# for item in added if value is key in subtracted, print added key and subtracted value
for (key, value) in added.items():
    if value in subtracted:
        sub_tup = subtracted[value]
        print(f"f({key[0]}) + f({key[1]}) = f({sub_tup[0]}) - f({sub_tup[1]}) == {f(key[0])} + {f(key[1])} = {f(sub_tup[0])} - {f(sub_tup[1])}")
