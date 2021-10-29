# Your code here
# initialize cache
cache = {}

def expensive_seq(x, y, z):
    # if x, y, z is in cache return value from cache
    if f"{x},{y},{z}" in cache:
        return cache[f"{x},{y},{z}"]
    # if x,y,z not in cache run logic, store solution in cache, and return solution
    else:
        if x <= 0:
            solution = y + z
            cache[f"{x},{y},{z}"] = solution
            return solution
        elif x > 0:
            solution = expensive_seq(x-1, y+1, z) + expensive_seq(x-2, y+2, z*2) + expensive_seq(x-3, y+3, z*3)
            cache[f"{x},{y},{z}"] = solution
            return solution


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
