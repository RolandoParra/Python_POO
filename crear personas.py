from classes import Human
from classes import coordenada
from classes import cuadrado

juan = Human("Pedro", "Perez Pereira", 387)
juan.show()
print()
lady = Human("Lady", "Gaga", 37)
lady.show()
print()
lady.apellidos = "Perez"
lady.show()

juan = lady
print()
juan.show()

print()
print()
print()

coord1 = coordenada(0, 1)
coord2 = coordenada(1, 1)
coord3 = coordenada(1, 0)
coord4 = coordenada(0, 0)

cuadrado1 = cuadrado(coord1, coord2, coord3, coord4)
cuadrado1.show()