def contient(n,d):
    if n%10 == d:
        res = True
    elif n%10 == n:
        res = False
    else:
        res = contient(n//10,d)
    return res

print(contient(7,7))