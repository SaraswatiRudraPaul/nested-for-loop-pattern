#5 5 5 5 5
#4 4 4 4
#3 3 3
#2 2
#1
num=int(input("enter number"))
for i in range(num):
    for j in range(num-i):
        print(num-i,end=" ")
    print( )