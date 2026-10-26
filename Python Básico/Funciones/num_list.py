def sum_list(numbers_list):
    result = 0
    for number in numbers_list:
        result = result + number
    return result
print(sum_list([1,5,6,8,3,4]))