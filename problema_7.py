"""
Control N°1

Nombre: Yerko Carreño Pérez
RUT: 18.245.437-0


Pregunta N°7

"""

### Solucion Problema N°7 #####

import math 
acum=0
print('N° de Meses')
p=int(input())


print('Ingrese tasa de interes  % ')
interes=float(input())/100

print('Monto')
monto= int(input())
for i in range(0,p):
  acum=monto+acum+(monto+acum)*interes
print(f'El monto final del ahorro en {p} meses a una tasa de interes del {interes*100} %, es ${acum}')