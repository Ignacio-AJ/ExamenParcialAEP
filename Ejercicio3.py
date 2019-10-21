cantidad = int(input("¿Cuántos productos va a registrar?"))
lista = []
for i in range(cantidad):
    num = str(i+1)
    nombre = input("Ingrese el nombre del producto" + num + ":")
    precio = float(input("Ingrese el precio del prodcuto" + num + ":"))
    categoria = input("Ingrese la categoría del producto" + num + ":")
    producto = [nombre,precio,categoria]
    lista.append(producto)
print(lista)
#Precio promedio
suma =0
for producto in lista:
    suma = suma + producto[1]
promedio = suma/cantidad
print("El precio promedio es:", promedio)
#Cantidad de productos que superan el precio promedio
contador = 0
for producto in lista:
    if producto[1]>promedio:
        contador+=1
print("Cantidad de productos que superan el precio promedio", contador)
#Producto mas caro
mas_caro=lista[0]
for producto in lista:
    if producto[1]> mas_caro[1]:
        mas_caro=producto
print("El producto mas caro es:", mas_caro)
#Prodcuto mas barato
mas_barato=lista[0]
for producto in lista:
    if producto[1]< mas_barato[1]:
        mas_barato=producto
print("El producto mas barato es:", mas_barato)
#Categoria mas alta
categorias = []
c = []
for p in lista:
    categoria = p[2]
    if categorias.count(categoria)==0:
        categorias.append(categoria)
        c.append(0)
    else:
        pos = categorias.index(categoria)
        c[pos]=c[pos]+1
mas_alto = max(c)
pos = c.index(mas_alto)
cat = categorias[pos]
print("La categoría con más productos es:",cat)