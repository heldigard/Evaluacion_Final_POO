from Medicamento import Medicamento
from Medico import Medico


class MedicamentoVentaRestringida(Medicamento):
    def __init__(
            self,
            sku,
            nombre_comercial,
            nombre_generico,
            precio_neto,
            peso,
            cantidad_stock,
            es_restringido,
            dosis_maxima,
            impuesto=0.19
    ):
        super().__init__(
            sku=sku,
            nombre_comercial=nombre_comercial,
            nombre_generico=nombre_generico,
            peso=peso,
            cantidad_stock=cantidad_stock,
            es_restringido=es_restringido,
            precio_neto=precio_neto,
            impuesto=impuesto
        )
        self.__dosis_maxima = dosis_maxima
        self.__medico: Medico = None

    @property
    def dosis_maxima(self):
        return self.__dosis_maxima

    @property
    def medico(self):
        return self.__medico

    @medico.setter
    def medico(self, medico):
        self.__medico = medico

    def __str__(self):
        mensaje = f"{super().__str__()}\t\
        Dosis: {self.__dosis_maxima:7}\t"
        if self.__medico:
            mensaje = mensaje + f"Medico: {self.__medico}"
        return mensaje
