import sys

def fibonnaci_recursivo(n):
    #Fibonnaci Clásico
    if(n == 0 or n == 1):
        return 1
    return fibonnaci_recursivo(n-1) + fibonnaci_recursivo(n-2)

def fixed_fibonnaci(n, memo = {}):
    #Fibonnaci Facherito
    if(n == 0 or n == 1):
        return 1
    try:
        return memo[n]
    except KeyError:
        resultado = fixed_fibonnaci(n-1, memo) + fixed_fibonnaci(n-2, memo)
        memo[n] = resultado

        return resultado

def main():
    sys.setrecursionlimit(10002) #Modifica la capacidad recursiva.
    n = int(input("Escoge un número: "))
    resultado = fixed_fibonnaci(n)
    print(resultado)

if __name__ == '__main__':
    main()

