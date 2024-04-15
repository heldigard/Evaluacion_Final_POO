from BaseDatos import BaseDatos


class Drogueria:

    def __init__(self, nombre, nit, telefono, ):
        self.__nombre = nombre
        self.__nit = nit
        self.__telefono = telefono
        self.__inventario = {}
        self.__db = BaseDatos()

    def inicializar_inventario(self):
        self.__inventario = self.__db.leer_inventario_desde_archivo(
            'MedicamentosInventario.csv'
        )

    def mostrar_inventario(self):
        for sku in self.__inventario.keys():
            medicamento = self.__inventario[sku]
            print(medicamento)


d = Drogueria('Drogueria', '123456789', '123456789')
d.inicializar_inventario()
d.mostrar_inventario()
