"""
Write a program that calculates & displays the letter

"""

score = float(input("input the score: "))
if 90 <= score <= 100:
    print("grade: A")
elif 80 <= score <= 89:
    print("grade: B")
elif score >= 70:
    print("grade: C")
elif score >= 60:
    print("grade: D")
elif score >= 0:
    print("grade: F")
else:
    print("Invalid score")