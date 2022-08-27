#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
num=int(input("enter number"))
for i in range(num):
    for j in range(i+1):
        print(j+1,end=" ")
    print( )