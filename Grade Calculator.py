#What is the Grade
grade = float(input("What is the grade percent"))

letter = ""

#figure out the grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >=70:
    letter = "C"
elif grade >=60:
    letter = "D"
else:
    letter = "F"

#get the last digit
last_digit = grade % 10
print(last_digit)

sign = ""
#determine the sign
if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"

# Handle exceptions (A+, F+, F-)
if letter == "A" and sign == "+":
    sign = ""
if letter == "F" and sign == "+" or "-":
    sign = ""

#display the letter of the grade
print (f"You have earned the grade {letter}{sign}")

if grade >= 70:
    print("Congratulation! You have passed the course!")
else:
    print("Sorry, please try the course again")

