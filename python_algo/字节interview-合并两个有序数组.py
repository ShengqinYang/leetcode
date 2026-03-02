



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


def merge_arrays(num1,num2):
    i,j = 0, 0
    new_num=[]
    while i< len(num1) and j<len(num2):
        if num1[i]<num2[j]:
            new_num.append(num1[i])
            i+=1
        else:
            new_num.append(num2[j])
            j+=1
    if num1[i:]:
        new_num.extend(num1[:1])
    if num2[j:]:
        new_num.extend(num2[j:])
    return new_num


if __name__=='__main__':
    num1 = [1, 4, 5, 6]
    num2 = [2, 3, 7, 10]
    print(merge_arrays(num1, num2))  # [1, 2, 3, 4, 5, 6, 7, 10]




