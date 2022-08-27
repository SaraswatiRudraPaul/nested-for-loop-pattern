#5
#5 4
#5 4 3
#5 4 3 2
#5 4 3 2 1
num=int(input("enter numbeer"))
for i in range(num):
    for j in range(i+1):
        print(num-j,end="")
    print( )