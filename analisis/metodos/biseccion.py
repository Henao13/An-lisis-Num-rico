from tabulate import tabulate

def C2_biseccion(f, a,b, tol,Nmax ):

    

    fa=f(a)
    fb=f(b)
    pm=(a+b)/2
    fpm=f(pm)
    E=1000 
    cont=0
    matriz = []

    while E>tol and cont<Nmax:
        if fb*fpm<0:
            a=pm; 
        else:
            b=pm;    
   
        p0=pm 
        pm=(a+b)/2 
        fpm=f(pm) 
        E=abs(pm-p0) 
        cont=cont+1 

         
         
        matriz.append([cont, a, fa, pm, fpm, b, fb, E ])

    return a, b, iter, matriz
    

def f(x):
    return x**3 - 7.51*x**2+18.4239*x-14.8331

a, b, iter, matriz = C2_biseccion(f, 3, 3.5, 0.0001, 30)

print(tabulate(matriz, headers=["Iteración", "a", "f(a)", "pm", "f(pm)", "b" , "f(b)" , "Error Abs." ], tablefmt="fancy_grid"))    
      
        
 