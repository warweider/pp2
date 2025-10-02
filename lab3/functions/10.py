def unique_list(lst):
    new = []
    for x in lst:
        if x not in new:
            new.append(x)
    return new

print(unique_list([1,2,2,3,4,4,5]))