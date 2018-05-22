import pickle

with open("Desktop\\temp.txt", 'w') as fobj:

    list1 = [1,2,3,4]

    pickle.dump(list1, fobj)
    
with open("Desktop\\temp.txt", 'r') as fobj:
    list2 = pickle.load(fobj)
    
    print list2
