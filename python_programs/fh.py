import pickle

with open("/home/msys/Desktop/temp", 'w') as fobj:

    list1 = [1,2,3,4]

    pickle.dump(list1, fobj)
    
with open("/home/msys/Desktop/temp", 'r') as fobj:
    list2 = pickle.load(fobj)
    
    print list2
