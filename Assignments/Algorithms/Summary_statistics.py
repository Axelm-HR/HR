import math

# Calculate the cumulative moving average and standard deviation
"""
lowercase_sigma = sqrt(sigma(xi - u)^2 / n)


xi = elements in data set (each element in list of numbers)
u = mean of the data set (mean of array)
n = size of the data set (lenght of the array)
lowercase_sigma = standard deviation
sigma = summation
-----------------------------------------------------------

lowercase_sigma = sqrt(sigma(xi - u)^2 / n) = population standard deviation
lowercase_sigma = sqrt(sigma(xi - u)^2 / n - 1) = sample standard deviation
"""

def standard_deviation_population(list_of_nums):
    current_average = sum(list_of_nums) / len(list_of_nums) # Cumulative moving average
    squared_sum = sum([math.pow((x - current_average), 2) for x in list_of_nums])
    standard_deviation = math.sqrt(squared_sum / len(list_of_nums))
    
    print("Average:", round(current_average, 2))
    print("Standard deviation:", round(standard_deviation, 2))


num_list = []


# Loop until the user types in -1
while True:
    try:
        user_num = int(input("Enter a number (-1 to exit) "))
        if user_num < 0:
            break
        else:
            num_list.append(user_num)
        standard_deviation_population(num_list)
    except ValueError:
        print("\n[!] Numbers Please!")
    except KeyboardInterrupt:
        print("\n[!] User Terminated")
        break
