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
        cabecera = f"{'SKU':2}\t\
                {'N. Comercial':15}\t\
                {'N. Generico':18}\t\
                {'Precio':1}\t\
                {'Peso':1}\t\
                {'Cant':1}\t\
                {'Restr':1}\t\
                {'IVA':1}\t\
                {'Info':1}"
        print("\nInventario de Medicamentos")
        print('-' * (len(cabecera) + 35))
        print(cabecera)
        print('-' * (len(cabecera) + 35))

        for sku in self.__inventario.keys():
            medicamento = self.__inventario[sku]
            print(medicamento)

    def mostrar_clientes(self):
        cabecera = f"{'Cedula':2}\t\
                {'Nombre':14}\t\
                {'Telefono':10}\t\
                {'Direccion':20}"
        print("\nLista de Clientes")
        print('-' * (len(cabecera) + 10))
        print(cabecera)
        print('-' * (len(cabecera) + 10))

        for cedula in self.__clientes.keys():
            cliente = self.__clientes[cedula]
            print(cliente)

    def mostrar_medicos(self):
        cabecera = f"{'Nombre':18}\t\
                {'Telefono':10}\t\
                {'Especialidad':20}"
        print("\nLista de Medicos")
        print('-' * (len(cabecera) + 10))
        print(cabecera)
        print('-' * (len(cabecera) + 10))

        for medico in self.__medicos:
            print(medico)
