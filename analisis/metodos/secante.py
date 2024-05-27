import math
from tabulate import tabulate
import sympy as sp
import re

def conversion(expr):
    expr = re.sub(r'(?<!\w)e', 'E', expr)


    expr = re.sub(r'\bln\b', 'log', expr)

    sympy_expr = sp.sympify(expr)


    converted_expr = str(sympy_expr).replace('E', 'math.exp(1)')


    converted_expr = converted_expr.replace('exp(', 'math.exp(')
    converted_expr = converted_expr.replace('log(', 'math.log(')

    return converted_expr



def secante(f, x0, x1, tol, Nmax):
    
    f =conversion(f) 
    
    def evaluate_expression(x):
        return eval(f)
    
    f0 = evaluate_expression(x0)
    f1 = evaluate_expression(x1)
    E = 0
    err=0
    cont = 0
    matriz = []
    E="-"
    err="-"
    matriz.append([cont, x0, f0, E, err])
    E = abs(x1 - x0)
    cont=1
    matriz.append([cont, x1, f1, E])
     
    while E > tol and cont < Nmax:
        cont = cont + 1


        denom = f1 - f0
        if denom == 0:
            print("Error: division por 0")
            break

        xact = x1 - f1 * (x1 - x0) / denom
        fact = evaluate_expression(xact)
        E = abs(xact - x1)


        if xact != 0:
            err = E / xact
        else:
            print("Error: division por 0")
            err = float('inf')

        matriz.append([cont-1, xact, fact, E, err]) 
        x0 = x1
        f0 = f1
        x1 = xact
        f1 = fact
         
    return matriz

 

f="e**-x - x"

matriz = secante(f, 0, 1, 10**-20, 100)

 


