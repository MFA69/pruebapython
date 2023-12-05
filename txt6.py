import json

usuario_contraseña = {}

def agregar(users):
  while True:
    usuario =input('ingrese nuevo usuario: ')
    if usuario == '' or usuario in usuario_contraseña:
      print ("usuario invalido")
    elif usuario != '':
      print ('usuario aceptado')
      #break
      check = False
      while check == False:
        contraseña = input('ingrese contraseña para registrar (4 digitos): ')
        contra_long = len(contraseña)
        if contraseña.isdigit() == False:
          check = False
          print (f'la contraseña debe ser solo numeros')
        elif contra_long < 4 or contra_long > 4:
          print (f"la contraseña debe contenter 4 digitos")
        else:
          print ('registro exitoso')
          users[usuario] = contraseña
          #guardar(users)
          return
          break

      key, value = usuario, contraseña
      users[key] = value
      return

def comprobar (users):
  comprueba_usuario = input("ingrese su usuario: ")
  if comprueba_usuario in usuario_contraseña:
    print (f"usuario registrado")
    intentos = 0
    while intentos != 3:
      posib_int = 3
      for i in range(posib_int):
        comp_contraseña = input("ingrese su contraseña: ")
        if comp_contraseña == usuario_contraseña[comprueba_usuario]:
          print ("la contraseña es correcta")
          return ("la contraseña es correcta")
          #break
        else:
          print('la contraseña es incorrecta.  %d intentos restantes' % (posib_int-i-1))
          intentos += 1
        if intentos == 3:
          print ('numero maximos de intentos')
          #return ('numero maximos de intentos')
  elif comprueba_usuario not in usuario_contraseña:
    print ("el usuario no existe")
    opcion = None    
    opcion = input("Marque 1 para registrar un nuevo usuario o presiones cualquier tecla para salir. ")
    while opcion != '1':
      #print('Has salido')
      return('Has salido')
      

      #opcion = input("Marque 1 para registrar un nuevo usuario o presiones cualquier tecla para salir. ")
        
        
        #opciones = {
            #'1': ('registrar nuevo usuario', accion1),
            #'2': ('ingrese cualquier tecla si quiere salir', salir)
            #}
          #print() # se imprime una línea en blanco para clarificar la salida por pantalla  
    else:
      agregar(usuario_contraseña)  
  #else:
   ##return ("el usuario no existe")
   #print ("el usuario no existe")

comprobar(usuario_contraseña)