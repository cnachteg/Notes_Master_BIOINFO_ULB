def pgcd(x,y):
    if y == 0:
        res = x
    else:
        res = pgcd(y,x%y)
    return res

print(pgcd(9,12))
print(pgcd(12,9))