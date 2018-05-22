str = raw_input("enter string : ")
freq = {}
for x in str:
    keys = freq.keys()
    if x in keys:
        freq[x] += 1
    else:
        freq[x] = 1
print sorted(freq)

