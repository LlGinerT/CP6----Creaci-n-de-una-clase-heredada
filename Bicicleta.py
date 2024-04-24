class Bicicleta:

    # c) Constructor de la clase bicicleta
    def __init__(self, marca, modelo, color) -> None:
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento

    def frenar(self, decremento):
        if self.velocidad >= decremento:
            self.velocidad -= decremento
        else:
            self.velocidad = 0

    def __str__(self) -> str:
        return f"Bicicleta {self.marca} {self.modelo} de color {self.color}, velocidad actual: {self.velocidad} Km/h"


class Moto(Bicicleta):

    # c) Constructor de la clase Moto
    def __init__(self, marca, modelo, color) -> None:
        """d) Atributos convertidos en protegidos.
        Un atributo publico en python, es aquel que se puede acceder
        y modificar desde fuera de la clase. Un atributo sin embargo,
        es aquel que la convención indica a otros programadores que no deberían
        acceder ni modificarlos desde fuera de la clase, aunque técnicamente python lo permita,
        para respetar el principio de encapsulación."""
        self._marca = marca
        self._modelo = modelo
        self._color = color
        self._velocidad = 0

    # Lo correcto para manejar estos atributos seria mediante
    # getters, setters y deleter
    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, nueva_marca):
        self._marca = nueva_marca

    @marca.deleter
    def marca(self):
        del self._marca

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, nueva_modelo):
        self._modelo = nueva_modelo

    @modelo.deleter
    def modelo(self):
        del self._modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, nueva_color):
        self._color = nueva_color

    @color.deleter
    def color(self):
        del self._color

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, nueva_velocidad):
        self._velocidad = nueva_velocidad

    @velocidad.deleter
    def velocidad(self):
        del self._velocidad

    # b) Método __str__ sobrecargado
    def __str__(self) -> str:
        return f"Moto {self.marca} {self.modelo} de color {self.color}, velocidad actual: {self.velocidad} Km/h"


def main():
    bici = Bicicleta("bmx", "j-500", "rojo")
    bici.acelerar(10)
    print(bici)
    moto = Moto("kawasaki", "Ninja", "verde")
    moto.acelerar(120)
    print(moto)
    moto.frenar(30)
    print(f"La moto después de frenar va a {moto.velocidad}Km/h")
    del moto.color
    moto.color = "azul"
    print(
        f"Después de quitarle el color a la moto, la hemos pintado de color {moto.color}"
    )


if __name__ == "__main__":
    main()
