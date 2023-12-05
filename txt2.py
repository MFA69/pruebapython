usuario_contraseña ={}

def agregar(users):
  with open("/Users/Usuario/OneDrive/Escritorio/python/ejerciciopython/pruebatxt/usu_cont.txt") as usu_cont:
    for linea in usu_cont:
      #print(linea)
      while True:
        usuario =input('ingrese nuevo usuario: ')
        if usuario == '' or usuario in linea:
          print ("usuario invalido")
        elif usuario != '':
          print ('usuario aceptado')
          #break
          check = False
          while check == False:
            contraseña = input('ingrese contraseña para registrar (4 digitos): ')
            contra_long = len(contraseña)
            if contraseña.isdigit() == False:
              check == False
              print (f'la contraseña debe ser solo numeros')
            elif contra_long < 4 or contra_long > 4:
              print (f"la contraseña debe contenter 4 digitos")
            else:
              print ('registro exitoso')
              break

          key, value = usuario, contraseña
          users[key] = value
          return

agregar(usuario_contraseña)

import json

ruta = '/Users/Usuario/OneDrive/Escritorio/python/ejerciciopython/pruebatxt'

def guardar (users):
  #login = open(ruta + "/usu_cont.txt","wt")
  login = open(ruta + "/usu_cont.txt","a")
  login2 = json.dumps(users)
  login.write(login2)
  login = json.loads(login2)
  return

guardar(usuario_contraseña)

def comprobar (users):
  with open("/Users/Usuario/OneDrive/Escritorio/python/ejerciciopython/pruebatxt/usu_cont.txt") as usu_cont:
    for linea in usu_cont:
        comprueba_usuario = input("ingrese su usuario: ")
        if comprueba_usuario in linea:
            print (f"usuario registrado")
            intentos = 0
            while intentos != 3:
                posib_int = 3
                for i in range(posib_int):
                    comp_contraseña = input("ingrese su contraseña: ")
                    if comp_contraseña == usuario_contraseña[comprueba_usuario]:
                        print("la contraseña es correcta")
                        #intentos == 3
                        return ("la contraseña es correcta")
                        #break
                    else:
                        print('la contraseña es incorrecta.  %d intentos restantes' % (posib_int-i-1))
                        intentos += 1
                    if intentos == 3:
                        return ('numero maximos de intentos')
        else:
            return ("el usuario no existe")

comprobar(usuario_contraseña)