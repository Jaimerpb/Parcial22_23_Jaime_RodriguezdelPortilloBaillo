class alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return f"El alumno  {self.nombre} se ha creado con exito"
    def __cali__(self):
        if self.nota>=5 and self.nota<=10:
            return f"El alumno {self.nombre} ha aprobado con un {self.nota}"
        elif self.nota<5 and self.nota>=0:
            return f"El alumno {self.nombre} ha suspendido con un {self.nota}"
