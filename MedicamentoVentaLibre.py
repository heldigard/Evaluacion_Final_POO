import Medicamento


class MedicamentoVentaLibre(Medicamento):
    def __init__(
            self,
            codigo,
            nombre_comercial,
            nombre_generico,
            peso,
            cantidad,
            sin_impuesto,
            contraindicaciones,
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
        self.contraindicaciones = contraindicaciones
