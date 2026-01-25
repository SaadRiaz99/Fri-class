print("---- Your Marksheet ----")

name = input("Enter your good name: ")
rollno = int(input("Enter your Roll No: "))

English = int(input("Enter English Marks (out of 100): "))
Maths = int(input("Enter Maths Marks (out of 100): "))
Science = int(input("Enter Science Marks (out of 75): "))
Urdu = int(input("Enter Urdu Marks (out of 100): "))
Islamiat = int(input("Enter Islamiat Marks (out of 50): "))
Programming = int(input("Enter Programming Marks (out of 75): "))

# Validation
if (English > 100 or Maths > 100 or Urdu > 100 or
    Science > 75 or Programming > 75 or Islamiat > 50):
    print(" Invalid marks entered!")
else:
    obt_marks = English + Maths + Science + Urdu + Islamiat + Programming
    percentage = (obt_marks / 500) * 100

    print("\n---- Result ----")
    print("Name:", name)
    print("Roll No:", rollno)
    print("Obtained Marks:", obt_marks)
    print("Percentage:", percentage, "%")

    if percentage >= 80:
        print("Grade: A+ 🎉")
    elif percentage >= 70:
        print("Grade: A")
    elif percentage >= 60:
        print("Grade: B")
    elif percentage >= 50:
        print("Grade: C")
    else:
        print("Fail ")
