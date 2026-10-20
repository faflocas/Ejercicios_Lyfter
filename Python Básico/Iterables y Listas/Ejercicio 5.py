my_list = []
print("You'll be asked for 10 different numbers")
for number in range (10):
    number = int(input("Enter a number: "))
    my_list.append(number)
max_list = max(my_list)
print(my_list, "The highest number is: ", max_list)