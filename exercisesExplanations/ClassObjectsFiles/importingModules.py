# Importa el paquete math
from math import radians
import math
# Definición del radio
r = 0.43

# Calcula C
C = 2 * math.pi * r

# Calcula A
A = math.pi * (r ** 2)

# Imprime los resultados
print("Circumference: " + str(C))
print("Area: " + str(A))

''' You can import genericly or selecting a part of the module
    1. import math
    2. from math import pi '''

# Definición de radio
r = 192500

# Importa la función radians del paquete math

# Distancia recorrida por la Luna en 12 grados. Guárdala dist.
phi = radians(12)
dist = r * phi

# Imprime dist
print(dist)
