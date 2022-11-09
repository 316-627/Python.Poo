class alumno:
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.nota=int(input("Ingrese la nota: "))
 
 
    def atributos(self):
        print("Nombre: ",self.nombre)
        print("nota: ",self.nota)
 
 
class Estudiante(alumno):
    def __init__(self):
        super().__init__()
        
 
 
    def atributos(self):
        super().atributos()
        print("NOTA: ",self.nota)
 
 
    def notas_calculo(self):
        if self.nota >=3:
         
          print("El alumno aprobo con una nota de: ", self.nota )
          
        else:
            print("El alumno reprobo con una nota de: ", self.nota)
 
persona1=alumno()
persona1.atributos()
estudent1=Estudiante()
estudent1.atributos()
estudent1.notas_calculo()
