def grade_classifier(score):
    if score >= 90:
        return "Distinction"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"

print(grade_classifier(95))
print(grade_classifier(85))
print(grade_classifier(60))
print(grade_classifier(45))
print(grade_classifier(100))

scores = [45, 72, 91, 60, 38, 85]
for score in scores:
    print(f"{score}: {grade_classifier(score)}")