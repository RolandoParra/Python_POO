from programa import Human

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