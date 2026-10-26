my_list = []
print("You'll be asked for 10 different numbers")
for number in range (10):
    number = int(input("Enter a number: "))
    my_list.append(number)
highest_number= my_list[0] 
for number in my_list:
    if number > highest_number:
        highest_number = number
print(my_list, "The highest number is: ", highest_number)
