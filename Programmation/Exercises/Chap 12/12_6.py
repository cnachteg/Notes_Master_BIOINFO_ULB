class Rational(object):
    def pgcd(self,x,y):
        if y == 0:
            res = x
        else:
            res = self.pgcd(y,x%y)
        return res

    def __init__(self, a = 0, b = 1):
        gcd = self.pgcd(a,b)
        self.a = a//gcd
        self.b = b//gcd

    def __str__(self):
        s = "{0}/{1}".format(self.a, self.b)
        return s

    def __repr__(self):
        s = "Rational({0},{1})".format(self.a, self.b)
        return s
    """def update(self,new_a,new_b):
        pgcd = self.pgcd(new_a,new_b)
        self.a = new_a//pgcd
        self.b = new_b//pgcd"""

    def __add__(self, other):
        if isinstance(other, int):
            new_a = (other*self.b) + self.a
            new_b = self.b
        elif isinstance(other, Rational):
            new_a = (other.a*self.b) + (self.a*other.b)
            new_b = other.b*self.b
        else:
            raise NotImplemented('op + only for int and Rational')
        return Rational(new_a,new_b)

    def __sub__(self, other):
        if isinstance(other, int):
            new_a =  self.a - (other*self.b)
            new_b = self.b
        elif isinstance(other, Rational):
            new_a = (self.a*other.b) - (other.a*self.b)
            new_b = other.b*self.b
        else:
            raise NotImplemented('op - only for int and Rational')
        return Rational(new_a,new_b)

    def __mul__(self, other):
        if isinstance(other, int):
            new_a =  self.a*other
            new_b = self.b
        elif isinstance(other, Rational):
            new_a = self.a*other.a
            new_b = other.b*self.b
        else:
            raise NotImplemented('op * only for int and Rational')
        return Rational(new_a,new_b)

    def __truediv__(self, other):
        if isinstance(other, int):
            new_other = Rational(1,other)
        elif isinstance(other, Rational):
            new_other = Rational(other.b,other.a)
        else:
            raise NotImplemented('op / only for int and Rational')
        return self.__mul__(new_other)

x = Rational(3,4)
y = Rational(1,2)
print(x*'a')