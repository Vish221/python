try:
    lst=list(eval(input("Enter the number")))
except SyntaxError:
    print("Length of list is 0")
a=[]
if(len(lst)==0):
    print("List length is 0")
for i in lst:
    if(i%5==0 and i<150):
        a.append(i)
print(a)        