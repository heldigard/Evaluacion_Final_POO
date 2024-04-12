import Medicamento
import Medico


class VentaRestringida(Medicamento):
    def __init__(
            self,
            codigo,
            nombre_comercial,
            nombre_generico,
            peso,
            cantidad,
            sin_impuesto,
            dosis_maxima,
            medico: Medico,
            impuesto=0.19
    ):
        super().__init__(
            codigo,
            nombre_comercial,
            nombre_generico,
            peso,
            cantidad,
            sin_impuesto,
            impuesto
        )
        self.__dosis_maxima = dosis_maxima
        self.__medico = medico
