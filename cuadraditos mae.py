from classes import coordenada
from classes import cuadrado

x1 = input("Ingrese la coordenada x del primer cuadrado: ")
y1 = input("Ingrese la coordenada y del primer cuadrado: ")

print()
x2 = input("Ingrese la coordenada x del segundo cuadrado: ")
y2 = input("Ingrese la coordenada y del segundo cuadrado: ")

print()
x3 = input("Ingrese la coordenada x del tercer cuadrado: ")
y3 = input("Ingrese la coordenada y del tercer cuadrado: ")

print()
x4 = input("Ingrese la coordenada x del cuarto cuadrado: ")
y4 = input("Ingrese la coordenada y del cuarto cuadrado: ")

print()
coord1 = coordenada(int(x1), int(y1))
coord2 = coordenada(int(x2), int(y2))
coord3 = coordenada(int(x3), int(y3))
coord4 = coordenada(int(x4), int(y4))

print()
cuadrado1 = cuadrado(coord1, coord2, coord3, coord4)
cuadrado1.show()