class Triangulo():
    def inicializar(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir(self):
        print("Valor lado 1:", self.lado1)
        print("Valor lado 2:", self.lado2)
        print("Valor lado 3:", self.lado3)

    def lado_mayor(self):
        if self.lado1 > self.lado2 and self.lado3:
            print("El lado mayor tiene un valor de: ", self.lado1 ,"y es el lado 1:")
        elif self.lado2 > self.lado1 and self.lado3:
            print("El lado mayor tiene un valor de: ", self.lado2 ,"y es el lado 2:")
        else: 
            self.lado3 > self.lado1 and self.lado2
            print("El lado mayor tiene un valor de: ", self.lado3 ,"y es el lado 3:")

    def triangulo_equilatero(self):
        if self.lado1 == self.lado2 and self.lado3:
            print("El triangulo es equilatero")
        else:
            print("El triangulo no es equilatero")

#Bloque principal
triangulo1 = Triangulo()
triangulo1.inicializar(4,4,4)
triangulo1.imprimir()
triangulo1.lado_mayor()
triangulo1.triangulo_equilatero()

triangulo2 = Triangulo()
triangulo2.inicializar(7,3,4)
triangulo2.imprimir()
triangulo2.lado_mayor()
triangulo2.triangulo_equilatero()