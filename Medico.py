from Persona import Persona


class Medico(Persona):
    def __init__(self, nombre, telefono, especialidad):
        super().__init__(nombre, telefono)
        self.__especialidad = especialidad

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, especialidad):
        self.__especialidad = especialidad
