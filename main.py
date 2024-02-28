#comentario de línea

'''
soy un comentario de bloque
'''

#DATOS PRIMITIVOS
nombreUsuario = "Jose Daniel"
edadUsuario = 34
estaturaUsuario = 1.75
estaLloviendo = True
notaPromedio = None

#ENTRADAS POR TECLADO
#numero1 = input('Digite el número 1: ')
#print(numero1)

#numero2 = input('Digite el número 2: ')
#print(numero2)

#PYTHON CASTEO DE DATOS

#DATOS HIDROITUANGO
userDB = "hidrotech123"
passwordBD = "admin123"
print('Software Tech Hidroituango')
print('**************************')
userName = input('Digita tu usuario: ')
userPasword = input('Digita tu contraseña: ')

if userDB==userName and passwordBD==userPasword:
    print('Exito en su usuario')
else:
    print('Fallaste')

'''print('Exito en su usuario')if userDB==userName and passwordBD==userPasword else print('Fallaste')'''

