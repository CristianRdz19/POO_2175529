class Alumno():
    def inicializar(self, nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre del alumno:", self.nombre)
        print("Nota:", self.nota)

    def mostrar_estado(self):
        if self.nota >= 4:
            print("Regular")
        else:
            print("No regular")

#Bloque principal
alumno1 = Alumno()
alumno1.inicializar("Cristian", 10)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2 = Alumno()
alumno2.inicializar("Omar", 3)
alumno2.imprimir()
alumno2.mostrar_estado()