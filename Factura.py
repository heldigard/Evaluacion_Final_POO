from Cliente import Cliente


class Factura:
    nit = "901456234-8"
    razon_social = "Droguería EIA SAS BIC"

    def __init__(self):
        self.__cliente: Cliente = None
        self.subtotal = 0
        self.total = 0
        self.empresa = "Droguería EIA SAS BIC"
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
        factura = f"{self.empresa}\n\n"
        factura += f"{'#Item':1}\t\
        {'Nombre':<20}\t\
        {'Peso':<1}\t\
        {'Precio':<1}\t\
        {'Cant':<1}\t\
        {'Subtotal':<8}\t\
        {'Total':<7}\n"
        for index, df in enumerate(self.detalles):
            factura += f"{index + 1} \t\
            {df}"
        factura += f"\nSubtotal: {self.subtotal}\nTotal: {self.total}\n"
        return factura
