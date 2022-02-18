# This project is to identify irreducible polynomials (deg<=3) in k[x] where k = \Z/n\Z
class Polynomial:
    def __init__(self, ceofs, field):
        self.coefs = ceofs
        self.field = field

    def evaluate(self, value):
        result = 0
        for i, coef in enumerate(self.coefs):
            result += coef * (value ** i)
        return result % self.field

    def is_irreducible(self):
        if not any(self.coefs[2:]):
            return True
        for i in range(self.field):
            if self.evaluate(i) == 0:
                return False
        return True

    def is_monic(self):
        ind = len(self.coefs)-1
        while self.coefs[ind]==0 and ind>0:
            ind-=1
        if self.coefs[ind]==1:
            return True

    def __str__(self):
        result = str(self.coefs[0]) if self.coefs!=0 else ""
        for i, coef in enumerate(self.coefs[1:]):
            result += " + {}{}{}".format(coef if coef!=1 else "","x**", i+1) if coef!=0 else ""
        return result

# Irreducible polynomials (deg<=3) in \Z_3[x]
polys = [Polynomial((i%3, i//3%3, i//9%3, i//27%3), 3) for i in range(81)]
count = 0
for poly in polys:
    if poly.is_irreducible() and poly.is_monic():
        count+=1
        print(poly)
print(count)
