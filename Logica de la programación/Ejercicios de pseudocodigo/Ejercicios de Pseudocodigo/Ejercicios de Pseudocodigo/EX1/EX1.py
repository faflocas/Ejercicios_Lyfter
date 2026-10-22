Ejrcicio 1 Cree un pseudocódigo que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que:
1.	Inicio 
2.	Definir precio_de_producto
3.	Definir descuento
4.	Definir precio_final
5.	Mostrar “ingrese precio del producto”
6.	Pedir precio_de_producto
a.	Si (precio_de_producto <100) entonces
7.	descuento = (precio_de_producto * 0.02)
a.	Sino
b.	Si (precio_de_producto >=100) entonces
8.	descuento = (precio_de_producto * 0.1)
a.	FinSi
9.	precio_final = precio - descuento
10.	Mostrar “Precio final”
11.	Mostrar precio_final
12.	Fin

Ejercicion 2 Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. Si es mayor, muestre “Mayor”. Si es exactamente igual, muestre “Igual”.

1.	Inicio
2.	Definir tiempo_segundos
3.	Definir contador
4.	Mostrar “Ingrese segundos”
5.	Pedir tiempo_segundos
6.	Contador = tiempo_segundos
a.	Si (contador < 600):
i.	Mostrar (600 – contador)
b.	Sino
i.	Si (contador = 600)
1.	Mostrar “Igual”
c.	Sino
i.	Si (contador > 600)
1.	Mostrar “Mayor”
d.	FinSi
7.	Fin

Ejercicio 3 Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado. Luego muestre el resultado de la suma.
1.	Inicio
2.	Definir numero
3.	Definir contador
4.	Definir resultado
5.	Mostrar “Ingrese numero”
6.	Pedir numero
7.	contador = 1
8.	resultado = 0
9.	Mientras que (contador <= numero) hacer:
a.	resultado = resultado + contador 
b.	contador = contador +1
10.	FinMIentras
11.	Mostrar “El resultado es”
12.	Mostrar resultado
13.	Fin