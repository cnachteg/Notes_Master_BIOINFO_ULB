class Monome:
    def __init__(self, coeff = 0.0, deg = 0 ):
        self.coeff = float(coeff)
        self.deg = deg
    def get_coefficient(self):
        return self.coeff
    def get_degre(self):
        return self.deg
    def __repr__(self):
        return "Monome({}, {})".format(self.coeff,self.deg)
    def __str__(self):
        if self.deg == 0:
            s = "{0:+}".format(self.coeff)
        elif self.deg == 1:
            s = "{0:+} x".format(self.coeff)
        else:
            s = "{0:+} x^ {1}".format(self.coeff,self.deg)
        return s
    def __add__(self, other):
        if self.deg != other.deg:
            raise Exception
        return Monome(self.coeff+other.coeff,self.deg)
    def __sub__(self, other):
        if self.deg != other.deg:
            raise Exception
        return Monome(self.coeff-other.coeff,self.deg)
    def __mul__(self, other):
        return Monome(self.coeff*other.coeff,self.deg+other.deg)
    def __truediv__(self, other):
        return Monome(self.coeff/other.coeff,self.deg-other.deg)
    def __floordiv__(self, other):
         return Monome(self.coeff//other.coeff,self.deg-other.deg)
    def __eq__(self, other):
        return self.deg == other.deg
    def __le__(self, other):
        return self.deg <= other.deg
    def __lt__(self, other):
        return self.deg < other.deg
    def __gt__(self, other):
        return self.deg > other.deg
    def __ge__(self, other):
        return self.deg >= other.deg

class Polynome:
    def __init__(self, *args):
        self.m = sorted(args)
        n = 0
        while n < len(self.m)-1:
            if self.m[n] == self.m[n+1]:
                self.m[n] += self.m[n+1]
                del self.m[n+1]
                if self.m[n].get_coefficient() == 0:
                    del self.m[n]
            else:
                n += 1
        if len(self.m) == 0:
            self.m = [Monome(0.0,0)]
        self.m = sorted(self.m)

    def __repr__(self):
        s = "Polynome("
        for i in range(len(self.m)-1):
            s += self.m[i].__repr__()
            s += ", "
        s += self.m[-1].__repr__()
        s += ")"
        return s

    def __str__(self):
        s = ""
        for i in range(len(self.m)-1,0,-1):
            s += self.m[i].__str__()
            s += " "
        s += self.m[0].__str__()
        return s

    def __add__(self, other):
        res = []
        for p1 in self.m:
            res.append(p1)
        for p2 in other.m:
            res.append(p2)
        return Polynome(*res)

    def __mul__(self, other):
        liste_m = []
        for m in self.m:
            for m_2 in other.m:
                liste_m.append(m * m_2)
        return Polynome(*liste_m)

q = Polynome(Monome(-2.0,4),Monome(2.0,4),Monome(2.0,4),Monome(35.0,1))
print(q)
print(q.__repr__())

p = Polynome(Monome(-2.0,4), Monome(3.0,5),Monome(9.0,0), Monome(-11.0,1))
print(p.__repr__())
print(p)

q = Polynome(Monome(-2.0,4), Monome(2.0,4))
print(q)

r = Polynome()
print(r)
print(r.__repr__())


p1 = Polynome(Monome(2,4), Monome(3,5), Monome(9,0))
p2 = Polynome(Monome(2,5), Monome(4,0), Monome(10,1))
p3 = p1 + p2
p4 = p1 * p2
print(p3)
print(p3.__repr__())
#+5.0 x^ 5 +2.0 x^ 4 +10.0 x +13.0
print(p4)
#6.0 x^ 10 +4.0 x^ 9 +30.0 x^ 6 +50.0 x^ 5 +8.0 x^ 4 +90.0 x +36.0