class Monome:
    def __init__(self, coeff = 1.0, deg = 0 ):
        self.coeff = float(coeff)
        self.deg = int(deg)
    def get_coefficient(self):
        return self.coeff
    def get_degre(self):
        return self.deg
    def __repr__(self):
        return "Monome({},{})".format(self.coeff,self.deg)
    def __str__(self):
        if self.deg == 0:
            s = "{}".format(self.coeff)
        elif self.deg == 1:
            if self.coeff > 0:
                s = "{0:+} x".format(self.coeff)
            else:
                s = "{0:-} x".format(self.coeff)
        else:
            if self.coeff > 0:
                s = "{0:+} x^ {1}".format(self.coeff,self.deg)
            else:
                s = "{0:-} x^ {1}".format(self.coeff,self.deg)
        return s

print(Monome(3,5))