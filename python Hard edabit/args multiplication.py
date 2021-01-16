def combinations(*items):
    result = 1
    for i in items:
        if i == 0:
            i = 1
        else:
            result *= i
    return result
print(combinations(6,7,0))

#42