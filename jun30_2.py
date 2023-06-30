# Dictionaries: Unordered & Mutable collection of key:value pairs
result = {"Maths":95, "Programming":100, "Physics":92, "English":95, "Maths":36}
"""
print(result)
# Accessing values through keys:
# print(result["Programming"])

# Modifying value of a key
result["Physics"] = 96
print(result)

# Adding new key:value pair
result["Python"] = 99
print(result)

# Deleting a key:value pair
del result["Maths"]
print(result)


# Altering "Maths":95 to "Science":95
# result["Science"] = 95
# del result["Maths"]
"""
# print(result)

d = {
    362001: ["Junagadh", "Joshipara"],      # numbers are allowed
    (380050, 380001, 380008, 380006) : ("Ghodasar", "Kalupur", "Naranpura", "Ellisbridge")      # tuple is allowed
}
print(d)