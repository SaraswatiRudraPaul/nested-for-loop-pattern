#5
#4 4
#3 3 3
#2 2 2 2
#1 1 1 1 1
num=int(input("enter number"))
for i in range(num):
    for j in range(i+1):
        print(num-i,end=" ")
    print( )