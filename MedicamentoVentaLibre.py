from Medicamento import Medicamento


class MedicamentoVentaLibre(Medicamento):
    def __init__(
            self,
            sku,
            nombre_comercial,
            nombre_generico,
            precio_neto,
            peso,
            cantidad,
            es_restringido,
            contraindicaciones,
            impuesto=0.19
    ):
        super().__init__(
            sku=sku,
            nombre_comercial=nombre_comercial,
            nombre_generico=nombre_generico,
            precio_neto=precio_neto,
            peso=peso,
            cantidad=cantidad,
            es_restringido=es_restringido,
            impuesto=impuesto
        )
        self.contraindicaciones = contraindicaciones

    def __str__(self):
        return f"{super().__str__()}\t\
        Contraindicaciones: {self.contraindicaciones}"
