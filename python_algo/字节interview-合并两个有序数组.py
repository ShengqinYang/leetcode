



def fun(num1, num2):
    res = []
    i, j = 0, 0
    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            res.append(num1[i])
            i += 1
        else:
            res.append(num2[j])
            j += 1
    if i < len(num1):
        res.extend(num1[i:])
    if j < len(num2):
        res.extend(num2[j:])
    return res


def merge_arrays(num1, num2):
    i, j=0, 0
    new_arr = []
    while i<len(num1) and j <len(num2):
        if num1[i] < num2[j]:
            new_arr.append(num1[i])
            i += 1
        else:
            new_arr.append(num2[j])
            j += 1
    new_arr.extend(num1[i:]) if num1[i:] else new_arr.extend(num2[j:])
    return new_arr


def merge_sort(arrays):
    if len(arrays) <= 1:
        return arrays   
    mid = len(arrays)//2
    left = merge_sort(arrays[:mid])
    right = merge_sort(arrays[mid:])
    return merge_arrays(left, right)


if __name__=='__main__':
    num1 = [1, 4, 5, 6]
    num2 = [2, 3, 7, 10]
    print(merge_arrays(num1, num2))  # [1, 2, 3, 4, 5, 6, 7, 10]
    
    arrays = [4,1,2,6,47,5,7,3]
    res = merge_sort(arrays)
    print(res)




