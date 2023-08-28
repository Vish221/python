#Question_1
n=int(input("Enter the number"))
for i in range (n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()  
#Question_2
n=int(input("Enter the number"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print() 
    
#Question_3
m=0
n=int(input("Enter the number"))
for i in range(n,0,-1):
    print(" "*m,end="")
    for i in range(i):
        print("*",end="")
    m+=1     
    print("")  
    
#Question_4
n=int(input("Enter the number"))
start=0
end=n-1
for i in range(n):
    print("*",end="")
print("")    
            
for i in range(n):
    for j in range(n):
        if(j==start or j==end):
            print("*",end="")
        else:
            print(" ",end="")
        
    print("")
    if(start==end):
        break
    start=start+1
    end=end-1 
#Question_5

n=int(input("Enter the number :"))
start=1
end=n-2
for i in range(n):
    print("*",end="")
print("") 
for i in range(n-1):
    for j in range(n):
        if(j>=start and j<=end):
            print("*",end="")
        elif(j<=start and j>=end):
            print("*",end="")
        else:
            print(" ",end="")
    print("")
    start+=1
    end-=1      
