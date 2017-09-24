def est_multiple(n,d):
    if n == d:
        res = True
    elif n < 0:
        res = False
    else:
        res = est_multiple(n-d,d)
    return res

print(est_multiple(16,3))
