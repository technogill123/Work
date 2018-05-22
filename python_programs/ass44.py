file=open("/home/msys/Desktop/lines.txt","r+")

count={}

for x in file.read().split():
    if x not in count:
        count[x] = 1
    else:
        count[x] += 1

for word,count in count.items():
    print word,count
