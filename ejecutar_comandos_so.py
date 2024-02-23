import os
import platform

print(platform.system())
print(platform.release())
comando = input('Ingres el comando a ejecutar: ')
rt = None
try:
    rt = os.system(comando)
except Exception as e:
    print(e)
if rt == 0:
    print('La ejecución fue correcta')
else:
    print('La ejecución no fue correcta')

