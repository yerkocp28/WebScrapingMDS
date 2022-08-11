"""
Control N°1

Nombre: Yerko Carreño Pérez
RUT: 18.245.437-0


Pregunta N°6

"""

### Solucion Problema N°6 #####

import math 

epsilon=0.001
x_actual=1

print('Ingrese el numero  NUM para obtener su raiz cubica')
num=math.fabs(int(input()))
aux=num

valor=1
i=0

while valor>epsilon:
    i+=1
    x_actual=(2*pow(x_actual,3)+num)/(3*pow(x_actual,2))  
    valor=math.fabs(x_actual-aux)
    aux=x_actual
    print(f'Iteracion numero {i} : {x_actual},  {valor} ')


print(f' numero de interaciones final {i} , Raiz cubica:{x_actual}' )