import random

def get_random_function(x):
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
        #'\\arcsin(' + x + ')',
        '\\arccos(' + x + ')',
        #'\\arctan(' + x + ')',
    ])
    
    return random.choice(functions)

def get_random_product(x):
    f = g = get_random_function(x)
    while f == g:
        g = get_random_function(x)
    return f + g

def get_random_chain(x):
    return get_random_function(get_random_function(x))

def get_random_quotient(x):
    f = get_random_function(x)
    g = get_random_function('x')
    return '\\frac{' + f + '}{' + g + '}'
