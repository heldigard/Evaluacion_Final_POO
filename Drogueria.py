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
        cabecera = f"{'SKU':8}\t\
        {'Nombre Comercial':20}\t\
        {'Nombre Generico':20}\t\
        {'Precio':6}\t\
        {'Peso':10}\t\
        {'Cant.':6}\t\
        {'Restr.':6}\t\
        {'Impuesto':4}\t\
        {'Info':4}"
        print(cabecera)
        for sku in self.__inventario.keys():
            medicamento = self.__inventario[sku]
            print(medicamento)


drogueria = Drogueria('Drogueria', '123456789', '123456789')
drogueria.inicializar_inventario()
drogueria.mostrar_inventario()
