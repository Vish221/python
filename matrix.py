graph="ABCDCA"
edge=[]
dict={'A':0,'B':1,'C':2,'D':3}
num=""
for i in graph:
    num=num+str(dict[i])    
matrix=[]
for i in range(len(graph)-1):
    if [graph[i],graph[i+1]] not in edge:
        edge.append([graph[i],graph[i+1]])
        edge.append([graph[i+1],graph[i]])
        matrix.append([int(num[i]),int(num[i+1])])
        matrix.append([int(num[i+1]),int(num[i])])
# print(matrix)
for i in range(4):
    for j in range(4):
        if([i,j] in matrix):
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()        
