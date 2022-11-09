class calculadora:
    def __init__(self):
        self.num1=int(input("Ingrese un numero entero: "))
        self.num2=int(input("Ingrese otro numero entero: "))
 
 
    def atributos(self):
        print("num1: ",self.num1)
        print("num2: ",self.num2)
 
 
class calculadora2(calculadora):
    def __init__(self):
        super().__init__()
        
 
 
    def atributos(self):
        super().atributos()
        print("numero: ",self.num2)
 
 
    def suma(self):
      s=self.num1 + self.num2
      print("resultado de suma: ",s)
    def resta(self):
      r=self.num1 - self.num2
      print("resultado de resta: ",r)
    def division(self):
      d=self.num1 / self.num2
      print("resultado de division: ",d)
    def multiplicacion(self):
      m=self.num1 * self.num2
      print("resultado de multiplicacion: ", m)
persona1=calculadora()
persona1.atributos()
estudent1=calculadora2()
estudent1.atributos()
estudent1.suma()
estudent1.resta()
estudent1.division()
estudent1.multiplicacion()
