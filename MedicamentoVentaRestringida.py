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
            cantidad,
            es_restringido,
            dosis_maxima,
            impuesto=0.19
    ):
        super().__init__(
            sku=sku,
            nombre_comercial=nombre_comercial,
            nombre_generico=nombre_generico,
            peso=peso,
            cantidad=cantidad,
            es_restringido=es_restringido,
            precio_neto=precio_neto,
            impuesto=impuesto
        )
        self.__dosis_maxima = dosis_maxima
        self.__medico: Medico = None

    @property
    def medico(self):
        return self.__medico

    @medico.setter
    def medico(self, medico):
        self.__medico = medico

    def __str__(self):
        return f"{super().__str__()}\t\
        Dosis: {self.__dosis_maxima:7}\t\
        Medico: {self.__medico}"
