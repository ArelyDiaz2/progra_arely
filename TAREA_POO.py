#TEMA 43
#PROBLEMA1
class Persona:
    def inicializar(self,nom):
        self.nombre=nom

    def imprimir(self):
      print('el nombre es:', self.nombre)


    persona1=Persona()
    persona1.inicializar('arely')
    persona1.imprimir()


#PROBLEMA 2
class Alumno :
  
      def inicializar(self,nomb,nota):
        self.nombre = nomb
        self.nota = nota

      def imprimir(self):
       print('su nombre es :' , self.nombre, 'su calificacion es :' , self.nota)

       def mostrar(self):
        if self.nota >=4:
            print('es regular')
        else:
            print('no es regular')


alumno1 = Alumno()
alumno1.inicializar('arely', 8)
alumno1.imprimir()
alumno1.mostrar()

#PROBLEMAS PROPUESTO 1
class Persona:
   def inicializacion(self,nom,edad):
     self.nombre = nom
     self.edad = edad


   def imprimir(self):
     print('el nombre es:',self.nombre)
     print('la edad es: ', self.edad)

     def mayor_edad(self):
        if self.edad >=18:
            print('es mayor de edad')

        else:
            print('no es mayor de edad')

persona1 = Persona()
persona1.inicializacion('arely' , 20)
persona1.imprimir()
persona1.mayor_edad()

#PROBLEMA PROPUESTO 2

class Triangulo:
  def inicializacion (self,l1,l2,l3):
    self.lado1 = l1
    self.lado2 = l2
    self.lado3 = l3

    def imprimir(self):
        if self.lado1 > self.lado2:
          int(input('el lado mayor es :', self.lado1))

        elif self.lado2 > self.lado3:
          int(input('el lado mayor es :', self.lado2))

        else:
            int(input('el lado mayor es :', self.lado3))


    def equilatero(self):
        if self.lado1 == self.lado2 and self.lado3:
          print('es equilatero')
        else:
          print('no es equilatero')
 

triangulo1 = Triangulo()
triangulo1.inicializacion(5,3,9)
triangulo1.imprimir()
triangulo1.equilatero()

#TEMA 44
# PROBLEMA1
class Empleado:
 
 def _init_(self):
   self.nombre = input('ingresa el nombre :')
   self.sueldo = float(input('ingresa el sueldo'))

def imprimir (self):
     print('nombre :',self.nombre)
     print('sueldo :',self.sueldo)

def impuestos (self):
   if self.sueldo >3000:
    print('debera pagar impuestos')

   else:
      print('no debera pagar impuestos')

      empleado1 = Empleado()
      empleado1.imprimir('arely', 3500)
      empleado1.impuestos()

#PROBLEMA 2
class Punto:

  def _init_(self,x,y):
    self.x = x
    self.y = y

  def imprimir (self):
    float(input('ingresa cordenada x', self.x))
    float(imput('ingresa cordenada y', self.y))


  def cuadrante(self):
    if self.x >x and self.y >y :
     print('primer cuadrante')

    elif self.x >x and self.y <y:
      print('segundo cuadrante')

    elif self.x <x and self.y >y:
      print ('tercer cuadrante')

    else:
      print('cuarto cuadrante')

punto1 = Punto
punto1.imprimir( 7,5)
punto1.cuadrante()

#PROBLEMA PROPUESTO 1 

class Cuadrado:
  def _init_(self,lado):
    self.lado = lado

  def imprimir(self):
    perimetro = self.lado * 4
    print('el perimetro es :' , perimetro)

    superficie = self.lado * self.lado
    print('la superficie es :', superficie)

cuadrado1 = Cuadrado()
cuadrado1.imprimir(9)

#PROBLEMA PROPUESTO 2
 
class Operaciones:
  def _init_(self):
   self.numero1 = int(input('ingresa el primer numero :'))
   self.numero2 = int(input('ingresa el segundo numero :'))
    

  def suma(self):
    suma = self.numero1 + self.numero2
    print('la suma es :',suma)

  def resta(self):
    resta = self.numero1 - self.numero2
    print('la resta es :', resta)

  def multiplicasion(self):
    multiplicasion = self.numero1 * self.numero2
    print('la multiplicasion es :', multiplicasion)

  def division(self):
    division = self.numero1 / self.numero2
    print('la division es :', division ) 


operacion1 = Operaciones()
operacion1.suma()
operacion1.resta()
operacion1.multiplicasion()
operacion1.division()