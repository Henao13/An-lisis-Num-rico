 
 
 
 
from django.shortcuts import render
from .metodos import biseccion,cholesky,crout,doolittle,facto_LU_gauss,gauss_piv,gauss_seidel,gauss_sencilla,incrementales,jacobi,newton, puntofijo,raices_m,regla_falsa,secante

 
  
def string_to_function(string):
    return lambda x: eval(string)

def analisis(request):
     
    metodo_seleccionado = None
    matriz = None

    if request.method == 'POST':
         
        form_type = request.POST.get('form_type')
        if form_type == 'form_seleccionar':
            metodo_seleccionado = request.POST.get('metodo')
             
        elif form_type == 'form_solucionar_in'  and 'f' in request.POST and 'x0' in request.POST and 'h' in request.POST and 'Nmax' in request.POST:
             
            f = string_to_function(request.POST.get('f'))
            Nmax = int(request.POST.get('Nmax'))
            x0 = int(request.POST.get('x0'))
            h = float(request.POST.get('h'))
            
             
            a, b, iter, matriz,h,f = incrementales.C1_busquedas(f, x0, h, Nmax)
            return render(request, 'analisis.html', {'metodo_seleccionado': metodo_seleccionado, 'matriz': matriz, 'a': a, 'b': b, "iter":iter, 'h': h, 'f': f})
        
        elif form_type == 'form_solucionar_bi' and 'f' in request.POST and 'a' in request.POST and 'b' in request.POST and 'tol' in request.POST and 'Nmax' in request.POST:
            f = string_to_function(request.POST.get('f'))
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            tol = float(request.POST.get('tol'))
            Nmax = int(request.POST.get('Nmax'))
            print("hola1") 
            
            a, b, iter, matriz1 = biseccion.C2_biseccion(f, a, b, tol, Nmax)
            return render(request, 'analisis.html', {'metodo_seleccionado': metodo_seleccionado, 'matriz1': matriz1, 'a': a, 'b': b, "iter":iter, 'f': f})
        
        elif form_type == 'form_solucionar_re' and 'f' in request.POST and 'a' in request.POST and 'b' in request.POST and 'tol' in request.POST and 'Nmax' in request.POST:
            f = string_to_function(request.POST.get('f'))
            a = float(request.POST.get('a'))
            b = float(request.POST.get('b'))
            tol = float(request.POST.get('tol'))
            Nmax = int(request.POST.get('Nmax'))
                      
            a, b, iter, matriz2 = regla_falsa.C3_reglaFalsa(f, a, b, tol, Nmax)
            return render(request, 'analisis.html', {'metodo_seleccionado': metodo_seleccionado, 'matriz2': matriz2, 'a': a, 'b': b, "iter":iter, 'f': f})
        
        if form_type == 'form_solucionar_pf' and 'g' in request.POST and 'x0' in request.POST and 'tol' in request.POST and 'Nmax' in request.POST:
            
            g= request.POST.get('g')
            x0 = float(request.POST.get('x0'))
            tol = float(request.POST.get('tol'))
            Nmax = int(request.POST.get('Nmax'))
            x, g,iter, matriz3 = puntofijo.punto_f(g, x0, tol, Nmax)
            return render(request, 'analisis.html', {'metodo_seleccionado': metodo_seleccionado, 'matriz3': matriz3, 'x': x, "iter":iter, 'g': g})
        
        if form_type == 'form_solucionar_rm' and 'f' in request.POST and 'df' in request.POST and 'd2f' in request.POST and 'x0' in request.POST and 'tol' in request.POST and 'Nmax' in request.POST:
            f = request.POST.get('f')
            df = request.POST.get('df')
            d2f = request.POST.get('d2f')
            x0 = float(request.POST.get('x0'))
            tol = float(request.POST.get('tol'))
            Nmax = int(request.POST.get('Nmax'))
            print("hola")
            matriz5= raices_m.C5_raices_mult(f, df, d2f, x0, tol, Nmax)
             
            return render(request, 'analisis.html', {'metodo_seleccionado': metodo_seleccionado, 'matriz5': matriz5})

        if form_type == 'form_solucionar_ne' and 'f' in request.POST and 'df' in request.POST and 'x0' in request.POST and 'tol' and 'Nmax' in request.POST:
            f = str(request.POST.get('f'))
            df = str(request.POST.get('df'))
            x0 = float(request.POST.get('x0'))
            tol = float(request.POST.get('tol'))
            Nmax = int(request.POST.get('Nmax'))
             
            matriz4 = newton.C5_newton(f,df, x0, tol, Nmax)
            return render(request, 'analisis.html', {'metodo_seleccionado': metodo_seleccionado, 'matriz4': matriz4})
        
        if form_type == 'form_solucionar_sec' and 'f' in request.POST and 'x0' in request.POST and 'x1' in request.POST and 'tol' in request.POST and 'Nmax' in request.POST:
            f = request.POST.get('f')
            x0 = float(request.POST.get('x0'))
            x1 = float(request.POST.get('x1'))
            tol = float(request.POST.get('tol'))
            Nmax = int(request.POST.get('Nmax'))
            matriz6 = secante.secante(f, x0, x1, tol, Nmax)
            return render(request, 'analisis.html', {'metodo_seleccionado': metodo_seleccionado, 'matriz6': matriz6})

        if form_type == 'form_solucionar_gas' and 'A' in request.POST and 'b' in request.POST:
            A= request.POST.get('A')
            b= request.POST.get('b')
            x = gauss_sencilla.gauss_sen(A, b)
            x = x.tolist()
            return render(request, 'analisis.html', {'metodo_seleccionado': metodo_seleccionado, 'x': x})
            
        if form_type == 'form_solucionar_gap' and 'A' in request.POST and 'b' in request.POST:
            A= request.POST.get('A')
            b= request.POST.get('b')
            x1 = gauss_piv.gauss_piv(A, b)
            x1 = x1.tolist()
            return render(request, 'analisis.html', {'metodo_seleccionado': metodo_seleccionado, 'x1': x1 })

        if form_type == 'form_solucionar_LU' and 'A' in request.POST and 'b' in request.POST:
            A= request.POST.get('A')
            b= request.POST.get('b')
            x2, L1, U1 = facto_LU_gauss.C11_lusimpl(A, b)
            L1 = L1.tolist()
            U1 = U1.tolist()
            x2 = x2.tolist()
            
            return render(request, 'analisis.html', {'metodo_seleccionado': metodo_seleccionado, 'L1': L1, 'U1': U1, 'x2': x2})
        

        if form_type == 'form_solucionar_doo' and 'A' in request.POST and 'b' in request.POST:
            A= request.POST.get('A')
            b= request.POST.get('b')
            L, U, xd = doolittle.doolittle(A, b)
            L = L.tolist()
            U = U.tolist()
            xd = xd.tolist()
            return render(request, 'analisis.html', {'metodo_seleccionado': metodo_seleccionado, 'L': L, 'U': U, 'xd': xd})
        
        if form_type == 'form_solucionar_cro' and 'A' in request.POST and 'b' in request.POST:
            A= request.POST.get('A')
            b= request.POST.get('b')
            L2, U2, x4 = crout.crout(A, b)
            L2 = L2.tolist()
            U2 = U2.tolist()
            x4 = x4.tolist()
            return render(request, 'analisis.html', {'metodo_seleccionado': metodo_seleccionado, 'L2': L2, 'U2': U2, 'x4': x4})
        
        if form_type == 'form_solucionar_cho' and 'A' in request.POST and 'b' in request.POST:
            A= request.POST.get('A')
            b= request.POST.get('b')
            L3 ,U3 ,x5 = cholesky.cholesky(A, b)
            L3 = L3.tolist()
            U3 = U3.tolist()
            x5 = x5.tolist()
            return render(request, 'analisis.html', {'metodo_seleccionado': metodo_seleccionado, 'L3': L3, 'U3': U3, 'x5': x5})
            
        if form_type == 'form_solucionar_jac' and 'A' in request.POST and 'b' in request.POST and 'x0' in request.POST and 'tol' in request.POST and 'Nmax' in request.POST:
            A= request.POST.get('A')
            b= request.POST.get('b')
            x0= request.POST.get('x0')
            tol = float(request.POST.get('tol'))
            Nmax = int(request.POST.get('Nmax'))
            matriz8 = jacobi.jacobi(A, b,x0,tol,Nmax)
            return render(request, 'analisis.html', {'metodo_seleccionado': metodo_seleccionado, 'matriz8': matriz8})
            
            
        if form_type == 'form_solucionar_gss' and 'A' in request.POST and 'b' in request.POST and 'x0' in request.POST and 'tol' in request.POST and 'Nmax' in request.POST:   
            A= request.POST.get('A')
            b= request.POST.get('b')
            x0=request.POST.get('x0')
            tol = float(request.POST.get('tol'))
            Nmax = int(request.POST.get('Nmax'))
            matriz7 = gauss_seidel.gauss_seidel(A, b ,x0 ,tol,Nmax)
            return render(request, 'analisis.html', {'metodo_seleccionado': metodo_seleccionado, 'matriz7': matriz7})
            

    return render(request, 'analisis.html', {'metodo_seleccionado': metodo_seleccionado })

                       
       
     
    

 
