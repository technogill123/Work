#ANMOL GILL
-Strings
1. Write a Python program to calculate the length of a string.

str = raw_input("enter the string:")
count = 0
for x in str:
    count=count+1
print count    


2. Write a Python program to count the number of characters (character frequency) in a string.
   Sample String : google.com'
   Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

str = raw_input("enter string : ")
freq = {}
for x in str:
    keys = freq.keys()
    if x in keys:
        freq[x] += 1
    else:
        freq[x] = 1
print sorted(freq)



3. Write a Python program to get a string from a given string where all occurrences of its first 
   char have been changed to '$', except the first char itself.
   Sample String : 'restart'
   Expected Result : 'resta$t'

str = raw_input("enter string : ")
first = str[0]
str = str.replace(first,'$')
str = first + str[1:]
print  str


4. Write a Python program to get a single string from two given strings, separated by a space 
   and swap the first two characters of each string.
    Sample String : 'abc', 'xyz' 
    Expected Result : 'xyc abz'

a = raw_input("enter str1 : ")
b = raw_input("enter str2 : ")
a1 = b[:2] + a[2:]
b1 = a[:2] + b[2:]
print a1 + ' ' + b1

5. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
   If the given string already ends with 'ing' then add 'ly' instead. 
   If the string length of the given string is less than 3, leave it unchanged.
    Sample String : 'abc'
    Expected Result : 'abcing' 
    Sample String : 'string'
    Expected Result : 'stringly'

str = raw_input("enter the string : ")
strlength = len(str)

if strlength > 2:
    if str[-3:] == 'ing':
       str = str + 'ly'
    else:
       str= str + 'ing'

print str




- Lists
1. Write a Python program to sum all the items in a list.

list = [0,1,2,55,7]
sum= 0 
for i in list:
    sum = sum + i
print sum


2. Write a Python program to get the largest number from a list.

list = [1,6,43,6,7,89,99]
largest=list[0]

for x in list:
    
    if x>largest:
        largest=x
print largest

3. Write a Python program to count the number of strings where the string length is 2 or more 
   and the first and last character are same from a given list of strings.
    Sample List : ['abc', 'xyz', 'aba', '1221']
    Expected Result : 2

list = ['1221','2232','666','4556','4644','1']
count = 0;


for x in list:
    if len(x) > 1:
        if x[0] == x[-1]:
            count = count + 1
print count

4. Write a Python program to get a list, sorted in increasing order by the last element in each 
   tuple from a given list of non-empty tuples.
    Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

list = [(2,1),(3,6),(7,8),(2,5),(8,9)]

print sorted(list, key=lambda x: x[1])



5. Write a Python program to remove duplicates from a list.

list = [1,3,23,234,2,3,23,3,4,324,4,6,6,4]
list1 = []
for x in list:
    if x not in list1:    
        list1.append(x)
print(list1)



- Dict
1. Write a Python script to add a key to a dictionary.

dict = {2:10,6:4,1:100}
dict.update({8:19})
print dict


2. Write a Python program to iterate over dictionaries using for loops.

dict = {'a':100,'u':23,'s':56}
for dict_key,dict_value in dict.items():
    print dict_key,dict_value


3. Write a Python script to check if a given key already exists in a dictionary.

dict = {'s':100,'p':2,'d':66}

user_input = raw_input("enter the key : ")
if user_input in dict:
    print "Key is present"
else:
    print"Key is not present"


4. Write a Python script to print a dictionary where the keys are numbers between 
   1 and 15 (both included) and the values are square of keys.
    Sample Dictionary 
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


dict = {}
for x in range (1,16):
    dict[x]=x*x
print dict

5. Write a Python program to sum all the items in a dictionary.

dict = {'s':100,'p':2,'d':66}
sum = 0
for dict_key,dict_value in dict.items():
    sum = sum + dict_value
print sum


- Tuple
1. Write a Python program to iterate over tuple using for loops.

tup = ("hi",6.89,45)
for x in tup:
    print x


2. Write a Python program to create a tuple with different data types 
   and print all the elements form the tuple.

tup = ('hi',3.66,9)
print tup


3. Write a Python program to find the repeated items of a tuple.

tup = (1,6,43,6,7,89,99)
user_input = input("enter the element : ")
if tup.count(user_input)>1:
    print "dublicate exists"
else:
    print "dublicate doesn't exists"


4. Write a Python program to check whether an element exists within a tuple.

tup = (1,4,23,41,3,1,23,3)

user_input = input()
if user_input in tup:
    print "yes it exists"
else:
    print "doesn't exists"


5. Write a Python program to find the length of a tuple.

tup = (1,32,42,4,1,13,431,6)
count = 0
for x in tup:
    count = count +1
print count

- Sets
1. Write a Python program to remove an item from a set if it is present in the set.

set1 = set([0,20,1,23,23,4,77,'s'])
print set1
n = raw_input("enter the element to be removed : ")
set1.discard(n)
print set1

2. Write a Python program to add member(s) in a set.

set1 = set([1,4,23,41,3,1,23,3,'a'])
print set1
user_input = raw_input("enter the element to add : ")
set1.update([user_input])
print set1

3. Write a Python program to iteration over sets.

set1 = set([1,4,23,5,345,25,6])

for x in set1:
    print x

4. Write a Python program to find the length of a set.

set1 = set([1,3234,253,62,3,2,24])
count = 0
for x in set1:
  count = count +1
print count;



