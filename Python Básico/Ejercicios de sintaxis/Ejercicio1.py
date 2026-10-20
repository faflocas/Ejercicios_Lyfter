print ("estatica" + "analoga")
#prints estaticaanaloga

print ("careful with the" + 28)
#  File "f:\Lyfter\Python\Ejercicios de sintaxis\Ejercicio1.py", line 3, in <module>
    print ("careful with the" + 28) 
TypeError: can only concatenate str (not "int") to str

list_1=[1,45,754,24]
list_2=[34,8,65,13,46]
print (list_1 + list_2)
#prints [1, 45, 754, 24, 34, 8, 65, 13, 46]

print ("careful with the" + list_1)
#prints  File "f:\Lyfter\Python\Tests.py", line 3, in <module>
    print ("careful with the" + list_1)
           ~~~~~~~~~~~~~~~~~~~^~~~~~~~
TypeError: can only concatenate str (not "list") to str

print (28 + "careful with the")
#prints  File "f:\Lyfter\Python\Tests.py", line 1, in <module>
    print (28 + "careful with the")
           ~~~^~~~~~~~~~~~~~~~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
