from BaseDatos import BaseDatos


class Drogueria:

    def __init__(self, nombre, nit, telefono, ):
        self.__nombre = nombre
        self.__nit = nit
        self.__telefono = telefono
        self.__inventario = {}

        self.inicializar_inventario()

    def inicializar_inventario(self):
        db = BaseDatos()
        self.__inventario = db.leer_inventario_desde_archivo(
            'MedicamentosInventario.csv'
        )
