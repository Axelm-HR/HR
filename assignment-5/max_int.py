# Logic: Write a program that find the maximum positive integer from user input.
# Algorithm: append all the numbers to a list and use the built-in method 'max()' to get the highest number in the list.


num_int = int(input("Input a number: "))
num_list = []
while num_int >= 0:
    num_int = int(input("Input a number: "))
    num_list.append(num_int)
print("The maximum is",max(num_list))
