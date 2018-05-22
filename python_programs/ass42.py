lines = 0
with open("/home/msys/Desktop/lines.txt", 'r') as f:
    for line in f:
        lines += 1
print "No. of lines in the file : ", lines
