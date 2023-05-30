#menuu para funciones

from conexion import DAO
import conexion
import funciones
def MenuPrincipal():
  conectar=DAO()
  bandera=True
  while bandera==True:
    print("### Menú PRINCIPAL ### ")
    print("1-Clientes")
    print("2-Registar Clientes")
    print("3-Actualizar Clientes")
    print("4-Borrar Clientes")
    print("5-Salir")
    op=int(input("Selecciona una Opción: "))
    if op>0 and op<6:
        if op==1:
            clientes=conectar.listarClientes()
            if len(clientes)>0:
                funciones.listar(clientes)
            else:
                print("No se pudo ejecutar la consulta")   
        elif op==2:
             datos=funciones.datosClientes()
             print(f"Estos datos son los que se van a insertar {datos}")
             try:
                 conectar.registrarClientes(datos)
             except:  
                print("No se pudo ejecutar el registro")     
        elif op==3:
             try:
                clientes=conectar.listarClientes()
                if len(clientes)>0 :
                   codigoCliente=funciones.datosClientesActualizar(clientes)
                   print(f"Campos codigoCliente {codigoCliente}")
                   if codigoCliente:
                      conectar.actualizarCliente(codigoCliente)
                   else:
                      print("Codigo no encontrado para Actualizar") 
                else:
                    print("No hay clientes") 

             except:  
                    print("No se pudo Actualizar el registro")       
        elif op==4:
             try:
                 clientes=conectar.listarClientes()
                 if len(clientes)>0 :
                   dato_Eliminar=funciones.registroEliminar(clientes)
                   print(f"Datos a eliminar {dato_Eliminar}")
                   if not(dato_Eliminar==""):
                       conectar.EliminarCurso(dato_Eliminar)
                   else:
                       print("Código del curso no encontrado...")
                 else:
                     print("No hay registros para Eliminar")      
             except:
                  print("Eliminar Except Master")
                                
        elif op==5:
             print("Hasta Luego")
             bandera=False
    else:
        print("Opció no valida selecciona una opción correcta")  
        
MenuPrincipal()              
              
        
    

  
