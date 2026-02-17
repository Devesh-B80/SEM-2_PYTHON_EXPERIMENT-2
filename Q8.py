"""Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects and
calculate the percentage.
CGPA=percentage/10
CGPA range:
0 to 3.4 -> F
3.5 to 5.0->C+
5.1 to 6->B
6.1 to 7-> B+
7.1 to 8-> A
8.1 to 9->A+"""
# take marks of five subjects
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

# calculate percentage
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

# calculate CGPA
cgpa = percentage / 10

# decide grade based on CGPA range
if 0 <= cgpa <= 3.4:
    grade = "F"
elif 3.5 <= cgpa <= 5.0:
    grade = "C+"
elif 5.1 <= cgpa <= 6.0:
    grade = "B"
elif 6.1 <= cgpa <= 7.0:
    grade = "B+"
elif 7.1 <= cgpa <= 8.0:
    grade = "A"
elif 8.1 <= cgpa <= 9.0:
    grade = "A+"
else:
    grade = "Out of range"

# display grade sheet
print("\n----- Grade Sheet -----")
print("Total Marks =", total)
print("Percentage =", percentage)
print("CGPA =", cgpa)
print("Grade =", grade)
