def longest():
   lines=open("/home/msys/Desktop/lines.txt", 'r')
   word=''
   for x in lines:
       if len(x)>len(word):
           word=x
   return word
print longest()
