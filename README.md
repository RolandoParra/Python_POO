# Python_POO

Introducción a la programació orientada a objetos en Python

## Por que aprender POO?

 - Imagina que quieres crear un **video jogo** tienes guerreros, magos, dragones... Cada Uno con sus propios puntos de vida, ataques y habilidades, como los organizo en código? sin repetir todo una y otra vez?

 - La **Programación Orientada a Objetos (POO)** es la respuesta! En lugar de escribir instrucciones sueltas, modelas el mundo real con ***objetos*** que tienen características y comportamientos, es la forma en que están construidos la mayoría de los programas profecionales del mundo

![XD](img/img_1.png)

## Clase y Objeto

 - Una clase es un tipo de dato cuyas variables se llaman "**Objetos**" ó "**Instancias**"

 - La clase es la definición del concepto del mundo real y los objetosó Instancias son el propio objeto del mundo real
 
 - Las clases están compuestas por 2 elementos:
    - **Atributos:** Informarción que almacena la clase
    - **Metodos:** Operaciones que pueden realizarse con la clase

## Definición de una clase en Python

``` Python
class NombreClase:
    def __init__(self, variable1, variable2):
        self.atributo1 = valor1
        self.atributo2 = valor2

    def nombreMetodo(self):
        bloquecodigo
```

- `class`: palabra reservada en Python para definir una clase reservada
- `NombreClase`: nombre de la clase que se quiere crear
- `def`: Palabra reservada en Python utilizada para definir tanto el constructor de la clase (método que se ejecuta la primera vez que se use una clase) cómo los diferentes métodos que tiene
- `__init__`: Palabra reservada en Python para definir el método constructor de la clase. El método `__init__` es lo primero que se ejecuta cuando creas un objeto de una clase.
- `(self, variableX)`: Parámetro del constructor de la clase. El parámetro **self** es obligatorio y despues puedes tener tantos parámetros como quieras. la forma de añadir parámetros es la misma que en las funciones
- `self.atributoX`: forma de utilización y acceso a los atributos de la clase.
- `NombreMetodo`: nombre del método de la clase
- `self`: parámetro del método. El parámetro **Self** es obligatorio y despues puedes tener tantos parámetros como quieras. la forma de añadir parámetros es la misma que las funciones
- `BloqueCodigo`: instrucciones que ejecuará el método
**Al definir una clase, tenga en cuenta**
- puedes definir tantos atributos como necesites
- puedes definir tantos métodos como necesites
- puedes definir tantos paŕametros en el constructor como necesites


![alt text](img/importante.jpeg)