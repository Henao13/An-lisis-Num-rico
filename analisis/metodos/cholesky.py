import numpy as np
import ast

def str_to_numpy_matrix(matrix_str):
    """
    Convierte una cadena de texto que representa una matriz o vector en un objeto numpy array.
    """
    try:
        # Evaluar la cadena para convertirla en una lista de listas (matriz) o una lista (vector)
        matrix_list = ast.literal_eval(matrix_str)
        
        # Convertir la lista en un array de numpy
        matrix_np = np.array(matrix_list, dtype=np.float64)
        
        return matrix_np
    except Exception as e:
        print(f"Error converting string to numpy matrix: {e}")
        return None

def sustprgr(A, b):
    # Inicialización
    n = A.shape[0]
    x = np.zeros(n)
    
    # Sustitución progresiva
    for i in range(n):
        sum_ax = 0
        for j in range(i):
            sum_ax += A[i, j] * x[j]
        
        # Verificar si el denominador es cero
        if A[i, i] == 0:
            print("Error: division por 0")
            continue

        x[i] = (b[i] - sum_ax) / A[i, i]
    
    return x

def sustregr(U, b):
    # Inicialización
    n = U.shape[0]
    x = np.zeros(n)
    
    # Sustitución regresiva
    for i in range(n-1, -1, -1):
        sum_ux = 0
        for j in range(i+1, n):
            sum_ux += U[i, j] * x[j]
        
        # Verificar si el denominador es cero
        if U[i, i] == 0:
            print("Error: division por 0")
            continue

        x[i] = (b[i] - sum_ux) / U[i, i]
    
    return x

def cholesky(A,b):
    A = str_to_numpy_matrix(A)   
    b = str_to_numpy_matrix(b)
    
    if np.all(np.linalg.eigvals(A) <= 0):
      return 0,0,0
    
    # Inicialización
    n = A.shape[0]
    L = np.eye(n)
    U = np.eye(n)
    
    # Factorización
    for i in range(n-1):
        L[i, i] = np.sqrt(A[i, i] - np.dot(L[i, :i], U[:i, i]))
        U[i, i] = L[i, i]
        for j in range(i+1, n):
            # Verificar si el denominador es cero
            if U[i, i] == 0:
                print("Error: division por 0")
                continue

            L[j, i] = (A[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]
        for j in range(i+1, n):
            # Verificar si el denominador es cero
            if L[i, i] == 0:
                print("Error: division por 0")
                continue

            U[i, j] = (A[i, j] - np.dot(L[i, :i], U[:i, j])) / L[i, i]
    L[n-1, n-1] = np.sqrt(A[n-1, n-1] - np.dot(L[n-1, :n-1], U[:n-1, n-1]))
    U[n-1, n-1] = L[n-1, n-1]
    
    z = sustprgr(L, b)
    x= sustregr(U, z)
    
    return L, U, x