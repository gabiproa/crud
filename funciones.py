#complementos del archivo master

def listar(clientes):
       print("\n Clientes \n")
       contador=0
       for cli in clientes:
           contador+=1
           print(f"{contador}-cliente con código: {cli[0]} Nombre: {cli[1]} Apellido: {cli[2]} y sus créditos son: {cli[3]}")
       print("#########\n")
           
def datosClientes():
     codigo=int(input("Dame el código: "))  
     nombre=input("Dame el nombre: ")     
     apellido=input("DAME EL APELLIDO: ")  
     creditos=int(input("Dame los crédito: ")) 
     
     clientes=(codigo,nombre,apellido,creditos)
     return clientes
 
def datosClientesActualizar(clientes):
     listar(clientes)#vemos todos los clientes
     existe=False
     codigoActualizar=int(input("Dame el código del cliente a Actualizar: "))
     for cli in clientes:
        print(cli[0])
        if cli[0]==codigoActualizar:
            print(f"Dato encontrado {codigoActualizar}")
            existe=True
            break 
     if existe:
       nombre=input("Dame el nombre: ")     
       apellido=input("DAME EL APELLIDO: ")  
       creditos=int(input("Dame los crédito: ")) 
       clientesE=(nombre,apellido,creditos,codigoActualizar)
     else:
         clientesE=None
     return clientesE
        
     
def registroEliminar(clientes):
  listar(clientes)
  existe=False
  codigoEliminar=int(input("Dame el código a Borrar: "))
  for cli in clientes:#recorro los campos
    print(cli[0])#muestro los campos
    if cli[0]==codigoEliminar:
      print("Dato encontrado")
      existe=True
      break
  if not existe:
    codigoEliminar=""      #sino lo encuentra devuelve vacio
  return codigoEliminar       #sino devuelve lo que encontro
     