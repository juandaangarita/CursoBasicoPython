def exchange_pesos_to_dollars (type_peso, dolar_value):
    pesos = float(input("¿How many pesos " + str(type_peso) + "do you want to convert?: "))
    dollars = round(pesos / dolar_value,2)
    print(str(pesos) + " pesos is equal to: " + str(dollars) + " USD dollars")


menu = """
Welcome to the money exchanger from pesos to dollaras 💲

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Please choose an option to wich type of pesos do you want to exchange:
"""
opcion = int(input(menu))

if opcion == 1:
    exchange_pesos_to_dollars("colombianos", 3785)
elif opcion == 2:
    exchange_pesos_to_dollars("argentinos", 65)
elif opcion == 3:
    exchange_pesos_to_dollars("mexicanos", 24)
else:
    print("Please choose a valid option")