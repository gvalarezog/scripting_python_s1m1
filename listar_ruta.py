import os
os.chdir('C:\\Proyectos\\Python\\Scripting\\Test1\\xx')
print(f'En la ruta: {os.getcwd()}')
for nombre in os.listdir():

    if os.path.isfile(nombre):
        print(f'Archivo: {nombre}')
    elif os.path.isdir(nombre):
        print(f'Directorio: {nombre}')

print('----------------')
# print(list(os.walk('C:\\Proyectos\\Python\\Scripting\\Test1')))
for elmento in list(os.walk('C:\\Proyectos\\Python\\Scripting\\Test1')):
    print(elmento)
print('----------------')

for r,d,f in list(os.walk('C:\\Proyectos\\Python\\Scripting\\Test1')):
    print(r)
    print(d)
    print(f)