class Persona:
    def inicializar(self,nombre):
        self.nombre = nombre

    def imprimir(self):
        print("Nombre:", self.nombre)

#bloque principal
Persona1 = Persona()
Persona1.inicializar("Cristian")
Persona1.imprimir()

Persona2 = Persona()
Persona2.inicializar("Omar")
Persona2.imprimir()