user_input = int(input("Input an integer (0 to quit): "))
sum_of_odd = 0
sum_of_even = 0
amount_odd = 0
amount_even = 0


while user_input != 0:
    try:
        if user_input % 2 == 0:
            amount_even += 1
            sum_of_even += user_input
        elif user_input < 0:
            print("Ignoring this negative numer!")
        else:
            amount_odd += 1
            sum_of_odd += user_input
        user_input = int(input("Input an integer (0 to quit): "))

    except Exception as e:
        print(e)

print("Sum of even:",sum_of_even)
print("Sum of odd:",sum_of_odd)
print("Even count:",amount_even)
print("Odd count:",amount_odd)