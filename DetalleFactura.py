from Medicamento import Medicamento
from MedicamentoVentaRestringida import MedicamentoVentaRestringida
from MedicamentoVentaLibre import MedicamentoVentaLibre


class DetalleFactura:
    def __init__(self, medicamento: Medicamento, cantidad=1):
        self.__medicamento: Medicamento = medicamento
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
        return (self.__medicamento.precio_neto * (self.__medicamento.impuesto + 1)) * self.__cantidad

    def calcular_subtotal(self):
        return self.__medicamento.precio_neto * self.__cantidad

    def __str__(self):
        mensaje = f"{self.medicamento.nombre_comercial:20}\t\
        {self.medicamento.peso:5}\t\
        {self.medicamento.precio_neto:10}\t\
        {self.cantidad:8}\t\
        {self.subtotal:>10}\t\
        {self.total:>2}\n"

        if type(self.medicamento) is MedicamentoVentaRestringida:
            mensaje = mensaje + self.texto_medicamento_restringido(self.medicamento)
        elif type(self.medicamento) is MedicamentoVentaLibre:
            mensaje = mensaje + self.texto_medicamento_libre(self.medicamento)

        mensaje = mensaje + "\n\n"
        return mensaje

    def texto_medicamento_restringido(self, medicamento: MedicamentoVentaRestringida):
        mensaje = f"Dosis: {medicamento.dosis_maxima:7}\t"
        if medicamento.medico:
            mensaje = mensaje + f"Medico: {self.__medico}"

        return mensaje

    def texto_medicamento_libre(self, medicamento: MedicamentoVentaLibre):
        mensaje = ""
        if len(medicamento.contraindicaciones) > 0:
            mensaje = f"Contraindicaciones: {medicamento.contraindicaciones}"

        return mensaje
