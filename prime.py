def countOfDigit(number):
    number=str(number)
    return(len(number))
def prime(start,end):
    if(isinstance(start, str)or isinstance(end, str)):
        print('Enter number instead of string')
        return
    elif(isinstance(start, float)or isinstance(end, float)):
        print("Number should be integer")
        return
    elif(start==0 or start<0):
        print("Zero or negative number not accepted")
        return
    elif(countOfDigit(start)>10 or countOfDigit(end)>10):
        print("Number digit should be less than 10")
        return
    for i in range(start,end):
        count=0
        for p in range(2,i):
            if(i%p==0):
                count+=1
        if(count==0):
            print(i)
prime(-25,192332423)                    