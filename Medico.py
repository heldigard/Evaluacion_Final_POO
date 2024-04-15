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

    def __str__(self):
        return f"{super().__str__()}\t\
        Especialidad: {self.especialidad}"
