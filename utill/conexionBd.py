
import mysql.connector

class conexionBd:

    def __init__(self) -> None:
        self.conexion = mysql.connector.connectççççççç8host="localhost ", database= "bdnotas", user="root", password="123456")
        
    def getconexionBd(self):
        return self.conexion
    