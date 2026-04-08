# retornar el valor maximo sin usar la función max()
def maximo(lista):
    if not lista:
        return None
    max_val = lista[0]
    for num in lista:
        if num > max_val:
            max_val = num
    return max_val

print("cuantos números desea ingresar?")
cantidad = int(input())
numeros = []
for i in range(cantidad):
    print(f"Ingrese el número {i + 1}:")
    num = float(input())
    numeros.append(num)
print(f"El número máximo en la lista es: {maximo(numeros)}")