#        1
#      2 1
#    3 2 1
#  4 3 2 1
#5 4 3 2 1
num=int(input("enter number"))
for i in range(num):
    for j in range(num-i-1):
        print(" ",end=" ")
    for j in range(i,-1,-1):
        print(j+1,end=" ")
    print( )