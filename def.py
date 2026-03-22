
def Area_circulo(radio):
    pi = 3.1416
    area = pi * radio ** 2
    return area

radio = float(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es: {Area_circulo(radio)}")

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Ingrese un número para verificar si es primo: "))
if es_primo(n):
    print(f"{n} es un número primo.")
else:
    print(f"{n} no es un número primo.")