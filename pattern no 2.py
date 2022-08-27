#5 4 3 2 1
#5 4 3 2
#5 4 3
#5 4
#5
num=int(input("enter nnumber"))
for i in range(num):
    for j in range(num-i):
        print(num-j,end=" ")
    print( )