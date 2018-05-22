list = [1,3,23,234,2,3,23,3,4,324,4,6,6,4]
list1 = []
for x in list:
    if x not in list1:    
        list1.append(x)
print(list1)
