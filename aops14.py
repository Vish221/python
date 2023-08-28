lst = [5, 4, 3, 5, 8, 1, 0, 9, 10, 9, 15]
res = []
for i in range(len(lst)-1):
    if i == 0:
        if lst[i + 1] > lst[i]:
            res.append(lst[i + 1])
        else:
            res.append(lst[i])
    elif lst[i] == len(lst) - 1:
        if lst[i] < lst[i - 1]:
            res.append(lst[i - 1])
    else:
        before = lst[i - 1]
        after = lst[i + 1]
        max_val = max(before, after)
        # print(type(max_val))
        print(max_val,end=" ")