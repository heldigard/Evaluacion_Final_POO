from Cliente import Cliente
from datetime import datetime
import random as ramdom


class Factura:
    def __init__(self, empresa, nit, razon_social):
        self.id = ramdom.randint(1000, 9999)
        self.empresa = empresa
        self.nit = nit
        self.razon_social = razon_social
        self.fecha = datetime.today()
        self.__cliente: Cliente = None
        self.subtotal = 0
        self.total = 0
        self.detalles = []

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    def agregar_detalle(self, detalle_factura):
        self.detalles.append(detalle_factura)

    def calcular_subtotal(self):
        subtotal = 0
        for df in self.detalles:
            subtotal += df.subtotal
        return subtotal

    def calcular_total(self):
        total = 0
        for df in self.detalles:
            total += df.total
        return total

    def facturar(self):
        self.subtotal = self.calcular_subtotal()
        self.total = self.calcular_total()

    def __str__(self):
        factura = f"{self.empresa}\n"
        factura += f"NIT: {self.nit}\n"
        factura += f"Razon Social: {self.razon_social}\n\n"
        factura += f"Factura: {self.id}\n"
        factura += f"Fecha: {self.fecha}\n\n"
        factura += f"Info Cliente\n"
        factura += self.texto_cliente()
        factura += f"{self.cliente}\n\n"
        factura += self.texto_encabezado()

        for index, df in enumerate(self.detalles):
            factura += f"{index + 1} \t\
            {df}"
        factura += f"\nSubtotal: {self.subtotal}\nTotal: {self.total}\n\n"

        return factura

    def texto_encabezado(self):
        return f"{'#Item':1}\t\
        {'Nombre':20}\t\
        {'Peso':8}\t\
        {'Precio':8}\t\
        {'Cant':1}\t\
        {'Subtotal':1}\t\
        {'Total':7}\n"

    def texto_cliente(self):
        return f"{'Cedula':10}\t\
        {'Nombre':20}\t\
        {'Telefono':18}\t\
        {'Direccion':10}\n"
