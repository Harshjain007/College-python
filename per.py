"""
write a program to calculate total marks in five subject(Full marks = 100) as well as percentage.
if per >= 80 print("a grade")
if per >= 60 print("b grade")
if per >= 40 print("c grade")
if per < 40 print("D grade")
"""
a = int(input("Enter marks in maths:"))
b = int(input("Enter marks in physics:"))
c = int(input("Enter marks in chemistry:"))
d = int(input("Enter marks in Hindi:"))
e = int(input("Enter marks in English:"))
total = (a + b + c + d + c) 
per = (total / 5)
Print("Total")
print("Total percentage is :" , per)
if per >= 80 :
	print("A grade")
elif per >= 60 :
	print("B grade")
elif per >= 40 :
    print("C grade")
else:
	print("D grade")
    