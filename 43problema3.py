class Persona():
    def inicializar(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir(self):
        print("Nombre:", self.nombre)
        print("Edad", self.edad)

    def mostrar_estado(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")
        
#Bloque principal
persona1 = Persona()
persona1.inicializar("Cristian", 20)
persona1.imprimir()
persona1.mostrar_estado()

persona2 = Persona()
persona2.inicializar("Omar", 17)
persona2.imprimir()
persona2.mostrar_estado()