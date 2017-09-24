def inverse(n):
    def expo(n):
        x = str(n)
        return len(x)-1
    if n//10 == 0:
        res = n
    else:
        i = expo(n)
        res = (n%10)*10**i + inverse(n//10)
    return res

print(inverse(4567))