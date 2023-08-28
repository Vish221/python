# build in function
number=[1,-2,-3,-4]
a=[]
for i in number:
    a.append(abs(i))
print(a)
# here is the map have two parameter abs and number
print(list(map(abs,number)))
#User defided fuction 
def multi(a,b):
    return a*b
list_1=[1,2,3,4]
list_2=[2,5,8,9]
print(set(map(multi,list_1,list_2)))

# Lambda Function
print(list(map(lambda a,b:a*b,list_1,list_2)))
