user_input = int(input("Input matrix size: "))
for i in range(1, (user_input*user_input)+1):
    print(i, end=' ')
    if i % user_input == 0:
        print("")
