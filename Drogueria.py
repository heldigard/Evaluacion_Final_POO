from BaseDatos import *
from Factura import Factura


class Drogueria:
    nit = "901456234-8"
    razon_social = "Droguería EIA SAS BIC"
    empresa = "Droguería EIA SAS BIC"

    def __init__(self, nombre, nit, telefono, ):
        self.__nombre = nombre
        self.__nit = nit
        self.__telefono = telefono
        self.__inventario = {}
        self.__clientes = {}
        self.__medicos = []
        self.__facturas = []

    @property
    def inventario(self):
        return self.__inventario

    @property
    def clientes(self):
        return self.__clientes

    @property
    def medicos(self):
        return self.__medicos

    @property
    def facturas(self):
        return self.__facturas

    def add_factura(self, factura: Factura):
        self.__facturas.append(factura)

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
                {'Nombre Comercial':15}\t\
                {'Nombre Generico':18}\t\
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

    def mostrar_inventario_cantidades(self):
        cabecera = f"{'SKU':2}\t\
                {'Nombre Comercial':15}\t\
                {'Cant':1}\t"
        print("\nResumen de Medicamentos")
        print('-' * (len(cabecera) + 5))
        print(cabecera)
        print('-' * (len(cabecera) + 5))

        for sku in self.__inventario.keys():
            medicamento = self.__inventario[sku]
            resumen = f"{sku:2}\t\
            {medicamento.nombre_comercial:20}\t\
            {medicamento.cantidad_stock}"
            print(resumen)

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

    def vender_medicamento(self, sku, cantidad):
        if sku in self.__inventario:
            if self.__inventario[sku].cantidad_stock >= cantidad:
                self.__inventario[sku].cantidad_stock -= cantidad
                return True
            else:
                return False

    def add_factura(self, factura: Factura):
        self.__facturas.append(factura)
