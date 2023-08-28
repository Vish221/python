str=input("Enter the string")
for i in range(len(str)):
    print(str.count(str[i]),end="")
    print(str[i],end="")