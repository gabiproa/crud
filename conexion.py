#todo lo que tiene que ver con la base de datos
import mysql.connector
from mysql.connector import Error

#conectando con mysql
class DAO:
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host="localhost",
                port=3306,
                user="gabriela2",
                password="1234",
                db="crud-poo"
            )
            print("conectado con Exito")
        except Error as ex:
            print(f"No se puede conectar a la base de datos{ex}")  
    def listarClientes(self):
        if self.conexion.is_connected():#estas conectado
            try:
                cliente=self.conexion.cursor()#cursor es palabra clave
                cliente.execute("SELECT * FROM clientes ORDER BY codigo ASC")  
                resultado=cliente.fetchall()#guarda en un array (lista, tupla, diccionario ["código","nombre","apellido","credito"])
                return resultado
            except Error as ex:
                print(f"No se pudo consultar Except {ex}")  
    def registrarClientes(self,curso):
        if self.conexion.is_connected():#estas conectado
            try:
                cliente=self.conexion.cursor()#cursor es palabra clave
                sql="INSERT INTO clientes (codigo,nombre,apellido,creditos)Values(%s,%s,%s,%s)"
               # curso=(3,"Pablo","Alvarez",32)
                cliente.execute(sql,curso)  
                self.conexion.commit()#ejecuta el código
                print("Registro guardado correctamente")
            
            except Error as ex:
                print(f"No se pudo registrar Except {ex}")
                
    def actualizarCliente(self,clientes):
        if self.conexion.is_connected():#estas conectado
            try:
                cliente=self.conexion.cursor()#cursor es palabra clave
                sql='UPDATE clientes SET nombre=%s, apellido=%s, creditos=%s WHERE codigo=%s'
               # curso=(3,"Pablo","Alvarez",32)
                cliente.execute(sql,clientes)  
                self.conexion.commit()#ejecuta el código
                print("Registro Actualizado correctamente")
            
            except Error as ex:
                print(f"No se pudo Actualizar Except conexión {ex}")                
      
    def EliminarCurso(self,curso_eliminar):
        if self.conexion.is_connected():
            try:
                cliente=self.conexion.cursor()
                print(f"Llego a conexión {curso_eliminar}")
                sql=f'DELETE FROM clientes WHERE codigo={curso_eliminar}'
                cliente.execute(sql)
                self.conexion.commit()
                print("Registro eliminado correctamente")
            except Error as ex:
                print(f"No se pudo Eliminar Except Conecion{ex}")               
#con=DAO()      
#print(con.listarClientes())
            