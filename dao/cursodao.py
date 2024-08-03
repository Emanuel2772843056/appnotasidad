
from utill.conexionBd import conexionBd

class cursodao:

    def __init__(self) -> None:
        self.conexion = conexionBd().getconexionBd()

    def listarcursos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT idcurso,nomcurso,credito FROM CURSO ORDER BY ORDER BY idcurso DESC"
        cursor.execute(sql)
        return cursor.fetchall()
    def insertarcurso(self, curso ):
        exec = self.conexion.cursor()
        sql = "INSERT INTO cursor VALUES('{}','{}','{}')".format(curso.codcurso, curso.nomcurso , curso.credcurso)
        exec.execute(sql)
        self.conexion.commit()
        exec.close()
        
    