#        1
#      2 2
#    3 3 3
#  4 4 4 4
#5 5 5 5 5
num=int(input("enter number"))
for i in range(num):
    for j in range(num-i-1):
        print(" ",end=" ")
    for j in range(i,-1,-1):
        print(i+1,end=" ")
    print( )