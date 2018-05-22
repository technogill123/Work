N = input("Enter the no. of lines you want to see :  ")
with open("/home/msys/Desktop/lines.txt", 'r') as fobj:
    lines = [next(fobj) for x in xrange(N)]
for word in lines:
    print word 
