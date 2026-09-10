print("========================================")
print("       STUDENT RESULT ANALYZER")
print("========================================")

name = input("Enter student name: ")

subjects = {}

subject_names = [
    "Python",
    "Mathematics",
    "Data Structure",
    "Artificial Intelligence",
    "English"
]

# Taking marks
for subject in subject_names:
    while True:
        try:
            marks = int(input("Enter marks in " + subject + " (0-100): "))

            if 0 <= marks <= 100:
                subjects[subject] = marks
                break
            else:
                print("Please enter marks between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

# Calculations
total = sum(subjects.values())
percentage = total / len(subjects)
average = percentage

# Grade
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 35:
    grade = "D"
else:
    grade = "F"

# Subject-wise result
subject_results = {}

for subject, marks in subjects.items():
    if marks >= 35:
        subject_results[subject] = "PASS"
    else:
        subject_results[subject] = "FAIL"

# Overall result
if all(marks >= 35 for marks in subjects.values()):
    overall_result = "PASS"
else:
    overall_result = "FAIL"

# Highest and lowest marks
highest_subject = max(subjects, key=subjects.get)
lowest_subject = min(subjects, key=subjects.get)

# Display result
print("\n========================================")
print("             STUDENT RESULT")
print("========================================")

print("Student Name:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Average Marks:", round(average, 2))
print("Grade:", grade)
print("Overall Result:", overall_result)

print("\n----------------------------------------")
print("        SUBJECT-WISE RESULT")
print("----------------------------------------")

for subject in subjects:
    print(
        subject,
        ":",
        subjects[subject],
        "-",
        subject_results[subject]
    )

print("\n----------------------------------------")
print("        PERFORMANCE SUMMARY")
print("----------------------------------------")

print(
    "Highest Marks:",
    highest_subject,
    "-",
    subjects[highest_subject]
)

print(
    "Lowest Marks:",
    lowest_subject,
    "-",
    subjects[lowest_subject]
)

print("========================================")
print("       END OF RESULT ANALYSIS")
print("========================================")
