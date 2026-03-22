

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {n} es: {factorial(n)}")
