lenght = int(input("Length of sequence: "))
step = int(input("Step size: "))

for i in range(step, (lenght*step)+1, step):
    print(i)
