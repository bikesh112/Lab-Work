

a=int(input("enter marks of maths"))
b=int(input("enter marks of science"))
c=int(input("enter marks of nepali"))
d=int(input("enter marks of opt maths"))
total_marks = a+b+c+d
print(f"total marks of all subject {total_marks}")
percentage= total_marks/4
print(f"percentage {percentage}")
if percentage>70:
    print("distinction")
elif percentage>60:

    print("first division")
elif percentage>40:

    print("pass")
else:
    print("fail")