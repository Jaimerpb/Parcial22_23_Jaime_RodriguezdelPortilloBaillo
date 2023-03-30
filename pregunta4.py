class alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
        print(f"El alumno ,de nombre {self.nombre}, se ha creado con éxito")
    
    def __cali__(self):
        if self.nota>=5 and self.nota<=10:
            return f"El alumno {self.nombre} ha aprobado con un {self.nota}"
        elif self.nota<5 and self.nota>=0:
            return f"El alumno {self.nombre} ha suspendido con un {self.nota}"
    
    def __str__(self):
        return f"Nombre:{self.nombre} | Nota: {self.nota}"


alumno1=alumno("Juan",5)
print(alumno1.__str__())
alumno2=alumno("Pedro",2)
print(alumno2.__str__())
alumno3=alumno("Maria",8)
print(alumno3.__str__())