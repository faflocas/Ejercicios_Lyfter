age = int(input("Input your age: "))
if (age <= 3):  
    print(f"You are a baby")
elif (age <= 10):
    print(f"You are a child")
elif (age <= 14):
    print(f"You are a preteen")
elif (age <= 17):
    print(f"You are a teenager")
elif (age <= 28):
    print(f"You are a young adult")
elif (age <= 65):
    print(f"You are an adult")
else:
    print(f"You are an old adult")