n=int(input("Enter the number"))
arr=[]
for i in range(97+n-1,96,-1):
    arr.append(chr(i))
for i in range(n+2):
    if(i%2!=0):
        for j in range(i):
            print(arr[p],end="")
        print()    