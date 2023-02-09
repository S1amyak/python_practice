def char_freq(s):
    d = {}
    for n in s:
        keys = d.keys()
        if n in keys:
            d[n] += 1
        else:
            d[n] = 1
    return d
print(char_freq("google.com"))
