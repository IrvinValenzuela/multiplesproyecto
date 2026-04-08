
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Ingrese un número para calcular su Fibonacci: "))
print(f"El Fibonacci de {n} es: {fibonacci(n)}")