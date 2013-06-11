import random

def GetStandardDerivableFunction(x):
    c = str(random.randint(2, 10))
    
    functions = ['{' + x + '}' + '^{' + c + '}']
    
    if x != 'x':
        functions = ['({' + x + '})' + '^{' + c + '}']
    
    functions.extend([
        'e^{' + x + '}',
        '{' + c + '}^{' + x + '}',
        '\\ln({' + x + '})',
        '\\log_{' + c + '}(' + x + ')',
        '\\sin(' + x + ')',
        '\\cos(' + x + ')',
        '\\tan(' + x + ')',
        '\\arcsin(' + x + ')',
        '\\arccos(' + x + ')',
        '\\arctan(' + x + ')',
    ])
    
    return random.choice(functions)

def GetChainOfStandardDerivableFunctions(x):
    return GetStandardDerivableFunction(GetStandardDerivableFunction(x))

def GetQuotientOfStandardDerivableFunctions(x):
    f = GetStandardDerivableFunction(x)
    g = GetStandardDerivableFunction('x')
    return '\\frac{' + f + '}{' + g + '}'
