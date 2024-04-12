class Persona:
 def __init__(self, nombre, telefono):
    self.__nombre = nombre
    self.__telefono = telefono

 @property
 def nombre(self):
   return self.__nombre

 @nombre.setter
 def nombre(self, nombre):
  self.__nombre = nombre

 @property
 def telefono(self):
   return self.__telefono

 @telefono.setter
 def telefono(self, telefono):
   self.__telefono = telefono

 def __str__(self):
    return f"Nombre: {self.nombre} - Teléfono: {self.telefono}"