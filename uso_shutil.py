import shutil
src='C:\\Proyectos\\Python\\Scripting\\argumentos\\Archivos\\src\\'
dst='C:\\Proyectos\\Python\\Scripting\\argumentos\\Archivos\\dst\\'
# print(dir(shutil))
# shutil.copyfile(src + 'prueba.txt', dst + 'prueba.txt') #prueba ls -lrt
# shutil.copy(src + 'prueba.txt', dst + 'prueba.txt') #prueba ls -lrt
# shutil.copy2(src + 'prueba.txt', dst + 'prueba.txt') #prueba ls -lrt
shutil.copymode(src + 'prueba.txt', dst + 'prueba.txt') #prueba ls -lrt