import os

print(os.sep)
print(os.getcwd())
os.chdir("C:\\Proyectos\\Python")
print(os.getcwd())
print(os.listdir())
print('----------------')
print(os.getcwd())
print(f'Los elemetos de la {os.getcwd()} ruta son: ')
for nombre in os.listdir():
    print(f'{nombre}')
print('----------------')
print(os.listdir("C:\\Proyectos"))
os.chdir('C:\\Proyectos\\Python\\Scripting')
try:
    os.mkdir('Test1')

except Exception as e:
    print('No se pudo crear el directorio porque ya exite', e)
print(os.listdir())
os.chdir('C:\\Proyectos\\Python\\Scripting\\Test1\\')
# os.makedirs('xx\\yy')
print('-'.center(50,'-'))
print(os.environ)
print(os.getpid())
print(os.getuid)