class Monome:
    def __init__(self, coeff = 0.0, deg = 0 ):
        self.coeff = coeff
        self.deg = deg
    def get_coefficient(self):
        return self.coeff
    def get_degre(self):
        return self.deg
    def __repr__(self):
        return "Monome({:.1f}, {})".format(self.coeff,self.deg)
    def __str__(self):
        if self.deg == 0:
            if self.coeff >= 0:
                s = "{0:+.1f}".format(self.coeff)
            else:
                s = "{0:-.1f}".format(self.coeff)
        elif self.deg == 1:
            if self.coeff >= 0:
                s = "{0:+.1f} x".format(self.coeff)
            else:
                s = "{0:-.1f} x".format(self.coeff)
        else:
            if self.coeff >= 0:
                s = "{0:+.1f} x^ {1}".format(self.coeff,self.deg)
            else:
                s = "{0:-.1f} x^ {1}".format(self.coeff,self.deg)
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
        if len(self.m) == 0:
            self.m = [Monome(0.0,0)]
        n = 0
        while n < len(self.m)-1:
            if self.m[n].get_degre() == self.m[n+1].get_degre():
                self.m[n] += self.m[n+1]
                del self.m[n+1]
            else:
                n += 1

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
        return Polynome(*(self.m+other.m))

    def __mul__(self, other):
        liste_m=[]
        for m in self.m:
            for m_2 in other.m:
                liste_m.append(m*m_2)
        return Polynome(*liste_m)

p1 = Polynome(Monome(2,4), Monome(3,5), Monome(9,0))
p2 = Polynome(Monome(2,5), Monome(4,0), Monome(10,1))
p4 = p1+p2
print(p4.__repr__())