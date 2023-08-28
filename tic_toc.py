import numpy as np
def tic_tac_toe(arr):
    arr_=['']
    for i in range(len(arr)):
        for j in range(1):
            if(arr[i][j]==arr[i][j+1]==arr[i][j+2]):
                return(arr[i][j])
    for j in range(len(arr)):
        for i in range(1):
            if(arr[i][j]==arr[i+1][j]==arr[i+2][j]):
                return(arr[i][j]) 
    arr_dum=np.array(arr)
    arr_=arr_dum.flatten()
    if(arr_[0]==arr_[4]==arr_[8]):
        return(arr_[0])            
    if(arr_[2]==arr_[4]==arr_[6]):
        return(arr_[2])
    return"Match Draw"
arr=[['x','x','o'],['o','o','x'],['x','o','x']]
print(tic_tac_toe(arr))
