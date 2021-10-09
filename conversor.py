menu = """
Bienvenido al conversor de monedas 😎

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción:
"""
opcion = int(input(menu))

if opcion == 1:
    pesos = float(input("¿Cuántos pesos colombianos deseas convertir a dolares?: "))
    valor_dolar = 3875
elif opcion == 2:
    pesos = float(input("¿Cuántos pesos argentinos deseas convertir a dolares?: "))
    valor_dolar = 65
elif opcion == 3:
    pesos = float(input("¿Cuántos pesos mexicanos deseas convertir a dolares?: "))
    valor_dolar = 24
else:
    print("Ingresa una opción valida")

dolares = round(pesos / valor_dolar,2)
print(str(pesos) + " pesos equivalen a: " + str(dolares) + " USD")