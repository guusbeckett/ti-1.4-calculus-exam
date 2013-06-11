import random

def get_random_function(x):
    c = str(random.randint(2, 10))
    
    functions = [
        c,
        x + '^{' + c + '}',
        '\\frac{1}{' + x + '}',
        'e^{' + c + x + '}',
        c + '^{' + x + '}',
        '\\ln(' + c + x + ')',
        '\\sin(' + c + x + ')',
        '\\cos(' + c + x + ')',
        '\\tan(' + c + x + ')',
        #'\\frac{1}{\\cos^2(' + c + x + ')}',
    ]
    
    return random.choice(functions)