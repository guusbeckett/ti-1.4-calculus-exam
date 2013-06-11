import random
from fractions import Fraction

class Function():
    def __init__(self):
        self.tex = ''
    
    def Add(self, tex):
        self.tex += ('+' if (self.tex != '' and len(tex) > 0 and tex[0] != '-') else '') + tex
        
    def Get(self):
        return self.tex
    
def Format_axN(a, n):
    if a == 0:
        return ''
    elif a == 1:
        if n == 1:
            return 'x'
        else:
            return 'x^{' + str(n) + '}'
    else:
        if n == 1:
            return str(a) + 'x'
        else:
            return str(a) + 'x^{' + str(n) + '}'
        
def FormatFraction(f):
    if f.numerator == f.denominator:
        return '1'
    elif f.numerator == 0:
        return '0'
    elif f.denominator == 1:
        return str(f.numerator)
    else:
        return '\\frac{' + str(f.numerator) + '}{' + str(f.denominator) + '}' 

def GetFraction():
    n = d = random.randint(2, 10)
    f = Fraction(n, d)
    while f.numerator == f.denominator:
        n = random.randint(2, 10)
        f = Fraction(n, d)
    return f
        
def GetNumberOrFraction():
    return random.choice([str(random.randint(2, 10)), FormatFraction(GetFraction())])
    
def Get_axN():
    return Format_axN(random.choice([-random.randint(1, 10), random.randint(1, 10)]), GetNumberOrFraction())

def Get_axN_bx_c():
    f = Function()
    f.Add(Get_axN())
    f.Add(Format_axN(random.randint(1, 10), str(random.randint(2, 10))))
    f.Add(str(random.randint(1, 10)))
    return f.Get()