def get_first_function():
    print("first function acquired")
    get_second_function()


def get_second_function():
    print("second function acquired")


get_first_function()