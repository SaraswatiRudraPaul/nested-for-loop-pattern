#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5
num=int(input("enter number"))
for i in range(num):
    for j in range(i+1):
        print(j+1,end=" ")
    print( )