str = raw_input("enter string : ")
first = str[0]
str = str.replace(first,'$')
str = first + str[1:]
print  str
