from Persona import Persona


class Cliente(Persona):
    def __init__(self, nombre, telefono, cedula, direccion):
        super().__init__(nombre, telefono)
        self.__cedula = cedula
        self.__direccion = direccion

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, cedula):
        self.__cedula = cedula

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion):
        self.__direccion = direccion

    def __str__(self):
        return f"{self.cedula:11}\t\
        {super().__str__()}\t\
        {self.direccion:20}"
