#write a program to display all even numbers that fall between two numbers (execlusive both numbers)entered by the user.
num=int(input("enter number"))
for i in range(1,11):
    if i%2==0:
        print(i)