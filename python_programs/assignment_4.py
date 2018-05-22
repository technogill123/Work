#ANMOL GILL

# 1. Write a Python program to read first n lines of a file.

N = input("")
with open("/home/msys/Desktop/lines.txt", 'r') as fobj:
    lines = [next(fobj) for x in xrange(N)]
print lines


# 2. Write a Python program to count the number of lines in a text file.

lines = 0
with open("/home/msys/Desktop/lines.txt", 'r') as f:
    for line in f:
        lines += 1
print "No. of lines in the file : ", lines


# 3. Write a python program to find the longest word in a file.

def longest():
   lines=open("/home/msys/Desktop/lines.txt", 'r')
   word=''
   for x in lines:
       if len(x)>len(word):
           word=x
   return word
print longest()


# 4. Write a Python program to count the frequency of words in a file.

file=open("/home/msys/Desktop/lines.txt","r+")
count={}
for x in file.read().split():
    if x not in count:
        count[x] = 1
    else:
        count[x] += 1
for word,count in count.items():
    print word,count


# 5. Write a Python program to read a file line by line and store it into a list.

with open("/home/msys/Desktop/lines.txt", 'r') as fobj:     
    content_list = fobj.readlines()
    print(content_list)


# 6. Write a Python program to append text to a file and display the text.

with open("/home/msys/Desktop/lines.txt",'wb') as f:
    f.write('Anmol')
with open("/home/msys/Desktop/lines.txt",'ab') as f:
    f.write('K')
with open("/home/msys/Desktop/lines.txt",'rb') as f:
    print f.read()


# 7. Write a Python program to write a list to a file. (write all the list elements to a file)

l1=['hi','hello','welcome']

with open("/home/msys/Desktop/lines.txt",'w') as f:
  f.write('\n'.join(l1))


# 8. Write a Python program to copy the contents of a file to another file

with open("/home/msys/Desktop/lines.txt") as fobj:
    with open("/home/msys/Desktop/copy.txt", "w") as fobj1:
        for line in fobj:
            fobj1.write(line)



