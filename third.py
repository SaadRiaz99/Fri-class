name = str(input("Enter your good name: "))
Rollno = int(input("Enter your Roll No: "))


English = int(input("Enter your English Marks: "))
Maths = int(input("Enter your Maths Marks: "))
Science = int(input("Enter your Science Marks: "))
Urdu = int(input("Enter your Urdu Marks: "))
Islamiat = int(input("Enter your Islamiat Marks: "))
Programing = int(input("Enter your Programming Marks: "))

obtmark = English + Maths + Science + Urdu + Islamiat + Programing

per = (obtmark /600) * 100
print("--------------------------------------------------")
print("Your Name is: ", name)
print("Your Roll No is: ", Rollno)
print("Your Obtained Marks is: ", obtmark)
print("Your Percentage is: ", per)


if per >= 80:
    print("Jani Pass ho gia Grade A+" ,  per, "%")
elif per >= 70:
    print("Jani Pass ho gia Grade A" ,  per, "%") 
elif per >= 60:
    print("Jani Pass ho gia Grade B" ,  per, "%")
elif per >= 50:
    print("Jani Pass ho gia Grade C" ,  per, "%")
else:
    print("Jani Fail ho gia mehnat kia kar bhai" ,  per , "%")       






 
# print(5 <= 6)       
# print(5 >= 6)       
# print(5 == 5)       
# print(6 != 5)
       


