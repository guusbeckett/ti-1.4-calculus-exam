from flask import Flask
from flask import render_template
from time import time

import random
import math

import functions
from functions import Function
import derivates
import integrals

app = Flask(__name__)

def generate_opgave1():
    # a)
    fraction = functions.GetFraction()
    
    f = Function()
    f.Add(functions.Format_axN(functions.FormatFraction(fraction), fraction.denominator))
    f.Add(functions.Get_axN())
    f.Add(derivates.GetStandardDerivableFunction('x'))
    
    # b)
    g = Function()
    p1 = random.choice(['(' + functions.Get_axN_bx_c() + ')', derivates.GetStandardDerivableFunction('x')])
    g.Add(p1 + derivates.GetStandardDerivableFunction('x'))
    
    # c)
    h = Function()
    h.Add(functions.GetNumberOrFraction() + derivates.GetChainOfStandardDerivableFunctions('x'))

    # d)
    i = Function()
    i.Add(derivates.GetQuotientOfStandardDerivableFunctions('x + ' + str(random.randint(1, 10))))
    
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
                        
                        f = Function()
                        f.Add(functions.Format_axN(a, 3))
                        f.Add(functions.Format_axN(b, 2))
                        f.Add(functions.Format_axN(c, 1))
                        f.Add(str(random.randint(1, 10)))
                              
                        return f.Get()
         
        c += 1


def generate_opgave3():
    # should probably check if people can work with exponents here...
    a = integrals.Wrap(functions.Get_axN() + '\\sqrt[' + str(random.randint(2, 10)) + ']{' + functions.Get_axN() + '}')
    b = integrals.Wrap(integrals.GetStandardFunction(derivates.GetStandardDerivableFunction('x')))
    
    # f(x)*g'(x) moet een functie zijn met een standaardintegraal
    
    # Pre-conditie: f'(x) heeft een standaardintegraal
    # Hoe blijft deze in stand?
    # a) Door g(x) te laten differentieren naar een constante.
    # of
    # b) Door f'(x) te laten integreren naar ax^n,
    #    verder g(x) te laten differentieren naar ax^q, zodanig dat:
    #    f(x) * g(x) = ax^(n+q)
    # alleen a) is uitgewerkt:
    g = functions.GetNumberOrFraction() + 'x'
    f_accent = integrals.GetStandardFunction('x')
    l = [g, f_accent]
    random.shuffle(l)
    c = integrals.Wrap(l[0] + l[1])
    
    # d)
    funcs = derivates.GetStandardFunctions('x')
    func = random.choice(funcs)
    d = integrals.Wrap(func[1] + integrals.GetStandardFunction(func[0]))
    
    return [a, b, c, d]

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