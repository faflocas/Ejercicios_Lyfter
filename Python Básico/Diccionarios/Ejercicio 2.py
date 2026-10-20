employee_dict = {}
keys = [
    "first_name",
    "last_name",
    "role"
]
values = [
    "Alek",
    "Castillo",
    "Software Engineer"
]
for item in range(len(keys)):
    employee_dict[keys[item]] = values[item]
print(employee_dict)