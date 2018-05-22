with open("/home/msys/Desktop/lines.txt",'wb') as f:
    f.write('Anmol')
with open("/home/msys/Desktop/lines.txt",'ab') as f:
    f.write('K')
with open("/home/msys/Desktop/lines.txt",'rb') as f:
    print f.read()
