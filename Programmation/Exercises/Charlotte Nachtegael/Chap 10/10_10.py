def concatenation(L1,L2):
    if len(L2) == 0:
        res = L1
    else:
        L1.append(L2[0])
        res = concatenation(L1,L2[1:])
    return res


L1 = [1,2]
L2 = [3,4]

print(concatenation(L1,L2))
