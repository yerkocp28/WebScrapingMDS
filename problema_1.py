"""
Control N°1

Nombre: Yerko Carreño Pérez
RUT: 18.245.437-0


Pregunta N°1

"""
### Solucion Problema N°1 #####

import math 

acum=0
print('Ingrese numero de iteraciones')
num=int(input())
print('Ingrese el valor de X, debe estar en grados sexagesimales(0° a 360°)')
x1= (input())


if x1.isdigit() is True and (float(x1)>=0) and (float(x1)<=360):
    x=math.radians(int(x1))
    for i in range(0,num):
     acum=acum+math.pow(-1,i)*((math.pow(x,(2*i+1)))/math.factorial(2*i+1))
    print(f'El valor del seno de {x1} es  {acum}  ')
else:
  print("Ingrese un Numero entre 0° y 360°")


