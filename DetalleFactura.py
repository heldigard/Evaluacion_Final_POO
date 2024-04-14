import Medicamento


class DetalleFactura:
    def __init__(self, medicamento: Medicamento, cantidad=1):
        self.__medicamento = medicamento
        self.__cantidad = cantidad
        self.__subtotal = self.calcular_subtotal()
        self.__total = self.calcular_total()

    @property
    def medicamento(self):
        return self.__medicamento

    @property
    def cantidad(self):
        return self.__cantidad

    @property
    def subtotal(self):
        return self.__subtotal

    @property
    def total(self):
        return self.__total

    def calcular_total(self):
        return (self.__medicamento.precio + self.__medicamento.valor_impuesto) * self.__cantidad

    def calcular_subtotal(self):
        return self.__medicamento.precio * self.__cantidad

    def __str__(self):
        return f"{self.medicamento}\t{self.cantidad:<8}\t{self.subtotal:<8}\t{self.total:<7}\n"
