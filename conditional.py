x = int(input("Enter a number: "))

# Basic if statement
if x > 0:
    print("x is positive")

# if-else statement
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

# if-elif-else statement
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Nested if statement
if x > 0:
    if x % 5 == 0:
        print("x is a multiple of 5")
    else:
        print("x is positive but not a multiple of 5")

# Short-hand (ternary) if-else
print("Even Number") if x % 2 == 0 else print("Odd Number")

# Using logical operators (and, or, not)
y = int(input("Enter another number: "))

if x > 0 and y > 0:
    print("Both numbers are positive")

if x > 0 or y > 0:
    print("At least one number is positive")

if not (x < 0):
    print("x is not negative")


x = 10  
print("Positive") if x > 0 else print("Negative or Zero")

#more examples require!
#1. Check if a Number is Positive, Negative, or Zero
x = int(input("Enter a number: "))
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

#2. Find the Largest of Two Numbers
a, b = 10, 20
print("Largest:", a if a > b else b)

#3.Check if a Number is Even or Odd

x = int(input("Enter a number: "))
print("Even") if x % 2 == 0 else print("Odd")

#4. Check Leap Year
year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


#5. Grading System
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#6. Check Vowel or Consonant
ch = input("Enter a letter: ").lower()
if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")


#7. Find the Largest of Three Numbers
a, b, c = 15, 25, 10
print("Largest:", max(a, b, c))


#8. Check if a Number is Divisible by 5 and 7
x = int(input("Enter a number: "))
if x % 5 == 0 and x % 7 == 0:
    print("Divisible by both 5 and 7")
else:
    print("Not divisible by both")

#9. Simple Login System
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Access Granted")
else:
    print("Access Denied")

#10. Day Name Based on Number (1-7)
day = int(input("Enter a number (1-7): "))
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[day - 1] if 1 <= day <= 7 else "Invalid input")
