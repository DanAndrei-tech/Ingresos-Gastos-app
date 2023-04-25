
# lectura de archivos
'''
with open('data/movimientos.csv','r')as resultado:
    leer = resultado.read()
    print(type(leer))
'''

#otro ejemplo
'''
resultado = open('data/movimientos.csv','r')
lectura = resultado.readlines()
print(lectura)
'''

import csv

midato = []
mifichero = open('data/movimientos.csv','r')
lectura = csv.reader(mifichero,delimiter=",",quotechar='"')

print(lectura)
for items in lectura:
    print(items)
    midato.append(items)

print("mi lista: ",midato[0])
