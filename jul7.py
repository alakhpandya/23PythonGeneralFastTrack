"""
menu = {
    "Parth" : "Punjabi",
    "Uday" : {"Dosa", "Sambhar", "Coca Cola"},
    "Harsh" : ["Soup", "Paneer Chilli", "Sabji-Naan", "Brownie with icecream"],
    "Prince" : 60,
    "Akshay" : ("roti", "4 subji", "daal", "sweets", "rice", "chhas"),
    "Khushi" : frozenset({"roti", "4 subji", "daal", "sweets", "rice", "chhas"}),
    "Hiral" : {
        "BF" : "Bread Butter",
        "Lunch" : "Punjabi",
        "Dinner" : "Gujarati"
    }
}
"""
# print(menu)
"""
Ask name from user
"""

result = {"Maths":95, "Programming":100, "Physics":92, "English":95, "Maths":36}
# result.clear()
r2 = result.copy()
r3 = result
"""
result.clear()
print(result)
print(r2)
print(r3)
"""
# print(result["Python"])
print(result.get("Python"))

