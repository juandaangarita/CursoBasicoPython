name = "Juan "
print (name)
name.upper()
print (name)
name = name.capitalize()
print (name)
name = name.strip()
print (name)
name.lower()
print (name)
name.replace('u','a')
print (name)
print (name[3])
print(len(name))

# Vamos a trabajar slices en texto

name = "Prueba de un nombre"
print(name[0:3])
print(name[:3])
print(name[3:])
print(name[:7])
print(name[1:7:2]) #inidice inicial:indice final:pasos, todos los criterios son opcionales
print(name[::-1]) # va desde el indice inicial al final per en forma inversa
