def div_entiere(n,d):
    x = n/d
    if n%d == 0:
        res = n/d
    else:
        res = div_entiere(n-1,d)
    return res
