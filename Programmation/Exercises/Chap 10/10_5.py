def triangle_pascal(i,j):
    if j == 0:
        res = 1
    elif i == 0 and j > 0:
        res = 0
    else:
        res = triangle_pascal(i-1,j) + triangle_pascal(i-1,j-1)
    return res

print(triangle_pascal(5,1))