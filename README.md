## ENUNCIADO:

Dado el sigueinte código de una clase Bicicleta:
```python
class Bicicleta:

def __init__(self, marca, modelo, color):

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

def __str__(self):

return f"Bicicleta {self.marca} {self.modelo} de color {self.color}, velocidad actual: {self.velocidad} km/h"
```
Se pide:

a) Crea una clase Moto que herede los métodos y atributos de la clase Padre Bicicleta.

b)  Utiliza la sobrecarga de métodos para la nueva clase hija con el método def __str__(self).

c)  Señala o remarca la parte del código donde se identifica el constructor de la clase.

d)  Convierte los atributos de la nueva clase en atributos protegidos y explica la diferencia con respecto a los públicos.
