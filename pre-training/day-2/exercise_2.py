students = [
    {"name": "Shahryar",  "scores": [85, 90, 78], "subject": "Math"},
    {"name": "Irtaza",    "scores": [92, 88, 95], "subject": "Physics"},
    {"name": "Naveed",    "scores": [70, 75, 80], "subject": "Chemistry"},
    {"name": "Waqas",     "scores": [88, 84, 91], "subject": "Biology"},
    {"name": "Akif",      "scores": [76, 82, 79], "subject": "Urdu"}
]

def calculate_average(scores):
    return sum(scores) / len(scores)

def get_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"

def class_topper(students):
    topper = students[0]
    for student in students[1:]:
        if calculate_average(student["scores"]) > calculate_average(topper["scores"]):
            topper = student
    return topper

topper = class_topper(students)
sorted_students = sorted(students, key=lambda s: calculate_average(s["scores"]), reverse=True)

# print(topper)
# print(sorted_students)

print(f"{'Name':<10} {'Subject':<15} {'Average':>10} {'Grade':>8} {'':>12}")
print("-" * 60)

for student in sorted_students:
    average = calculate_average(student["scores"])
    grade = get_grade(average)
    tag = "*** TOP ***" if student["name"] == topper["name"] else ""

    print(f"{student['name']:<10} {student['subject']:<15} {average:>10.2f} {grade:>8} {tag:>12}")