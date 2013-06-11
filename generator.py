from flask import Flask
from flask import render_template
from time import time
from fractions import Fraction
import random
import math
import derivates
import integrals
app = Flask(__name__)

class TFunction():
    def __init__(self):
        self.tex = ''
    
    def Add(self, tex):
        self.tex += ('+' if (self.tex != '' and tex[0] != '-') else '') + tex
        
    def Get(self):
        return self.tex

class TFraction(Fraction):
    def __init__(self, *args):
        super(TFraction, self).__init__(*args)
    
    def Get(self):
        if self.numerator == self.denominator:
            return '1'
        elif self.numerator == 0:
            return '0'
        elif self.denominator == 1:
            return str(self.numerator)
        else:
            return '\\frac{' + str(self.numerator) + '}{' + str(self.denominator) + '}' 

def fmt(a, n):
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

def get_random_fraction():
    n = d = random.randint(2, 10)
    f = TFraction(n, d)
    while f.numerator == f.denominator:
        n = random.randint(2, 10)
        f = TFraction(n, d)
    return f

def get_random_number():
    return random.choice(['-', '']) + str(random.randint(2, 10))

def get_random_number_or_fraction():
    return random.choice([get_random_number(), get_random_fraction().Get()])

def get_random_ax_n():
    return fmt(get_random_number(), get_random_number_or_fraction())

def generate_opgave1():
    # a)
    fraction = get_random_fraction()
    
    f = TFunction()
    f.Add(fmt(fraction.Get(), fraction.denominator))
    f.Add(get_random_ax_n())
    f.Add(get_random_number_or_fraction() + derivates.get_random_function('x'))
    
    # b)
    g = TFunction()
    g.Add(get_random_number_or_fraction() + derivates.get_random_product('x'))
    
    # c)
    h = TFunction()
    h.Add(get_random_number_or_fraction() + derivates.get_random_chain('x'))

    # d)
    i = TFunction()
    i.Add(derivates.get_random_quotient('x + ' + str(random.randint(1, 10))))
    
    return [f.Get(), g.Get(), h.Get(), i.Get()]

def generate_opgave2():
    # Zoek een gedifferieenterde functie ax^2 + bx + c, zodanig dat:
    # a = 3 (a / 3 door primitiveren moet 1 zijn)
    # b % 2 == 0 (b / 2 door primitiveren moet geheel zijn)
    # b^2 - 4ac = q^2 (discriminant is een kwadraat)
    
    a = 3
    c = random.randint(-10, 10)
     
    while True:
        for q in range(0, 100):
            val = q**2 + 4*a*c
             
            if val >= 0:
                b = math.sqrt(val) 
                 
                if b == int(b):
                    b = int(b)
                     
                    if int(b) % 2 == 0:
                        # Primitiveer
                        
                        a /= 3 #redunant
                        b /= 2
                        c /= 1
                        
                        f = TFunction()
                        f.Add(fmt(a, 3))
                        f.Add(fmt(b, 2))
                        f.Add(fmt(c, 1))
                        f.Add(str(random.randint(1, 10)))
                              
                        return f.Get()
         
        c += 1


def generate_opgave3():
    f = integrals.get_random_function('x')
    g = integrals.get_random_function(derivates.get_random_function('x'))
    h = integrals.get_random_function('x') + derivates.get_random_function('x')
    return ['\\int ' + f + ' \\mathrm{d}x', '\\int ' + g + ' \\mathrm{d}x', '\\int ' + h + ' \\mathrm{d}x']

def generate_opgave4():
    return []

@app.route("/")
def random_exam():
    return exam(time())

@app.route("/<seed>")
def exam(seed=0):
    seed = int(seed)
    random.seed(seed)

    opgaves = {}
    opgaves['opgave1'] = generate_opgave1()
    opgaves['opgave2'] = generate_opgave2()
    opgaves['opgave3'] = generate_opgave3()
    opgaves['opgave4'] = generate_opgave4();
    
    return render_template('exam.html', seed=seed, **opgaves)

if __name__ == "__main__":
    app.run(debug=True)