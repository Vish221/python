a={1:"Stedent abc",2:"Student BCD",3:"Student CDE"}
lst=[10,20,10,30,40,30,50]
result={}
idx=0
for item in lst:
    if item in result:
        print("Item Exists")
        indexlist=result[item]
        indexlist.append(idx)
        result[item]=indexlist
    else:
        indexlist=[idx]
        result[item]=indexlist
    idx+=1
print(result)            