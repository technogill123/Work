list = ['1221','2232','666','4556','4644','1']
count = 0;


for x in list:
    if len(x) > 1:
        if x[0] == x[-1]:
            count = count + 1
print count

