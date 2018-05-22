str = raw_input("enter the string : ")
strlength = len(str)

if strlength > 2:
    if str[-3:] == 'ing':
       str = str + 'ly'
    else:
       str= str + 'ing'

print str

