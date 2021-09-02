n = int(input("Enter the length of the sequence: ")) # Do not change this line
num_list = [0, 1, 2]
final = [1, 2]
for i in range(0, n-2):
    num = sum(num_list)
    final.append(num)
    num_list.append(num)
    num_list.pop(0)

for elements in final:
    print(elements)