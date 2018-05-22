with open("/home/msys/Desktop/lines.txt") as fobj:
    with open("/home/msys/Desktop/copy.txt", "w") as fobj1:
        for line in fobj:
            fobj1.write(line)
