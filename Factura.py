class Factura:
    nit = "901456234-8"
    razon_social = "Droguería EIA SAS BIC"

    def __init__(self):
        self.subtotal = 0
        self.total = 0
        self.empresa = "Droguería EIA SAS BIC"
        self.detalles = []

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
        factura += f"{'Código':6}\t{'Nombre':15}\t{'Precio':7}\t{'Impuesto':8}\t{'Cantidad':8}\t{'Subtotal':8}\t{'Total':7}\n"
        for df in self.detalles:
            factura += f"{df}"
        factura += f"\nSubtotal: {self.subtotal}\nTotal: {self.total}\n"
        return factura
