def unique_lisy(l):
    x = []
    for i in l:
        if i not in x:
            x.append(i)
    return x
print(unique_lisy([1,2,3,4,4,5,5,5,6]))
