# Dictionaries, do you mean Map, Json or XML?
# Key value structures

empty_dict = {}
grades = {"Joel":80, "John":10}
joel_grade = grades["Joel"]

try:
    kate_grade = grades["Kate"]
except KeyError:
    "No grade for Kate!"

print("Joel" in grades)
print("Kate" in grades)

# For no error, use get method
joel_grade = grades.get("Joel") # This is 80
kate_grade = grades.get("Kate") # This is None
kate_grade = grades.get("Kate", 0) # This is 0

grades["John"] = 80 # Modify value
grades["Kate"] = 90 # Create new entry
print(len(grades))  # I know, I know, it could be a method....

grades_keys = grades.keys()
grades_values = grades.values()
grades_items = grades.items()