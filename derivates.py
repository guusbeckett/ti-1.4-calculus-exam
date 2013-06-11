import random
import functions

def GetStandardFunctions(x):
    c = str(random.randint(2, 10))

    x = (x if x == 'x' else ('(' + x + ')'))

    fs = [
        ('{' + x + '}' + '^{' + c + '}', functions.Format_axN(c, int(c)-1)),
        ('e^{' + x + '}', 'e^{' + x + '}'),
        ('{' + c + '}^{' + x + '}', '\\ln(' + c + ')'),
        ('\\ln({' + x + '})', '\\frac{1}{' + x + '}'),
        ('\\log_{' + c + '}(' + x + ')', '\\frac{1}{\\ln{' + c + '}}\\frac{1}{' + x + '}'),
        ('\\sin(' + x + ')', '\\cos(' + x + ')'),
        ('\\cos(' + x + ')', '-\\sin(' + x + ')'),
        #'\\tan(' + x + ')',
        #'\\arcsin(' + x + ')',
        #'\\arccos(' + x + ')',
        #'\\arctan(' + x + ')',
    ]
    
    return fs

def GetStandardDerivableFunction(x):
    return random.choice(GetStandardFunctions(x)[0])

def GetChainOfStandardDerivableFunctions(x):
    return GetStandardDerivableFunction(GetStandardDerivableFunction(x))

def GetQuotientOfStandardDerivableFunctions(x):
    f = GetStandardDerivableFunction(x)
    g = GetStandardDerivableFunction('x')
    return '\\frac{' + f + '}{' + g + '}'
