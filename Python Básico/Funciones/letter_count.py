def count_letters(text):
        uppercase = 0 
        lowercase = 0
        for char in text:
            if char.isupper():
                uppercase += 1
            if char.islower():
                lowercase += 1
        print(f"The amount of uppercase letters is {uppercase}, the amount of lowercase letters is {lowercase}")


count_letters(input("Enter your sentence "))