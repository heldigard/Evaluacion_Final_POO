from BaseDatos import *


class Drogueria:

    def __init__(self, nombre, nit, telefono, ):
        self.__nombre = nombre
        self.__nit = nit
        self.__telefono = telefono
        self.__inventario = {}
        self.__clientes = {}
        self.__medicos = []

    def inicializar_datos(self):
        self.__inicializar_inventario()
        self.__inicializar_clientes()
        self.__inicializar_medicos()

    def __inicializar_inventario(self):
        self.__inventario = leer_inventario_desde_archivo(
            'MedicamentosInventario.csv'
        )

    def __inicializar_clientes(self):
        self.__clientes = leer_clientes_desde_archivo(
            'Clientes.csv'
        )

    def __inicializar_medicos(self):
        self.__medicos = leer_medicos_desde_archivo(
            'Medicos.csv'
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
        print('-' * (len(cabecera) + 35))
        print(cabecera)
        print('-' * (len(cabecera) + 35))

        for sku in self.__inventario.keys():
            medicamento = self.__inventario[sku]
            print(medicamento)

    def mostrar_clientes(self):
        cabecera = f"{'Cedula':6}\t\
                {'Nombre':8}\t\
                {'Telefono':10}\t\
                {'Direccion':20}"
        print('-' * (len(cabecera) + 15))
        print(cabecera)
        print('-' * (len(cabecera) + 15))

        for cedula in self.__clientes.keys():
            cliente = self.__clientes[cedula]
            print(cliente)


drogueria = Drogueria('Drogueria', '123456789', '123456789')
drogueria.inicializar_datos()
drogueria.mostrar_clientes()
