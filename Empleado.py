class Persona:

    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))
 
 

    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
 
 
class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))
 
 
    def mostrar(self):
        super().mostrar()
        print("Sueldo: ",self.sueldo)
 
 
    def pagar_impuestos(self):
        if self.sueldo > 3600000:
          d=self.sueldo-(self.sueldo*3.5)/100
          a=self.sueldo-d
          print("El total a ganar con descuento de 3,5% es de:",d )
          print("se le desconto un valor total de", a)
        else:
            print("El total a ganar es de", self.sueldo)
 
persona1=Persona()
persona1.mostrar()
empleado1=Empleado()
empleado1.mostrar()
empleado1.pagar_impuestos()
