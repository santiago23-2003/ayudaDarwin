import json
#Lista que ya esta
productos = '{"mangueras": 39, "arandelas": 94, "puntillas": 44}'
#Convirtiendo la lista a un dicc
diccionario = json.loads(productos)
#Valores que se ingresan
recibirProductos = str(input())
#Aqui pasa el string a una lista para poder compararla
productosConvertidos = recibirProductos.split(' ')
#cajas que hay  
totalCajas = []
#Total de las cajas
sumaDeCajas = 0
#Productos que estan 
productosQueEstan = []

for producto in productosConvertidos:
  if (producto in diccionario):
    totalCajas.append(diccionario[producto])
    productosQueEstan.append(producto)
  
for cajasQueEstan in totalCajas:
    sumaDeCajas += cajasQueEstan

print(sumaDeCajas)
print(' '.join(productosQueEstan))
