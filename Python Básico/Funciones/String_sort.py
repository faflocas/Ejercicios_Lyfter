def regular_string(my_string):
    word_list = my_string.split("-")
    word_list.sort()
    sorted_string = "-".join(word_list)
    return sorted_string


print(regular_string("python-variable-funcion-computadora-monitor" ))