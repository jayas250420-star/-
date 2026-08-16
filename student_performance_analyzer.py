name = input("Enter student name: ")

tamil = int(input("Enter Tamil mark: "))
english = int(input("Enter English mark: "))
maths = int(input("Enter Maths mark: "))
python = int(input("Enter Python mark: "))
physics = int(input("Enter Physics mark: "))

total = tamil + english + maths + python + physics

average = total / 5

# Finding highest mark
highest = tamil

if english > highest:
    highest = english

if maths > highest:
    highest = maths

if python > highest:
    highest = python

if physics > highest:
    highest = physics


# Finding lowest mark
lowest = tamil

if english < lowest:
    lowest = english

if maths < lowest:
    lowest = maths

if python < lowest:
    lowest = python

if physics < lowest:
    lowest = physics


print("\n------ Student Report ------")
print("Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)


# Result and Grade

if tamil >= 35 and english >= 35 and maths >= 35 and python >= 35 and physics >= 35:

    print("Result: PASS")

    if average >= 90:
        print("Grade: A")
        print("Performance: Excellent")

    elif average >= 75:
        print("Grade: B")
        print("Performance: Very Good")

    elif average >= 50:
        print("Grade: C")
        print("Performance: Good")

    else:
        print("Grade: D")
        print("Performance: Need Improvement")

else:
    print("Result: FAIL")
    print("Suggestion: Practice more and improve marks")