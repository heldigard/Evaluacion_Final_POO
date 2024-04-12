class Medicamento:

    def __init__(
            self,
            sku,
            nombre_comercial,
            nombre_generico,
            precio_neto,
            peso,
            cantidad,
            impuesto=0.19
    ):
        self.__sku = sku
        self.__nombre_comercial = nombre_comercial
        self.__nombre_generico = nombre_generico
        self.__precio_neto = precio_neto
        self.__peso = peso
        self.__cantidad = cantidad
        self.__impuesto = impuesto

        self.__calcular_precio_bruto()

    @property
    def sku(self):
        return self.__sku

    @property
    def precio_neto(self):
        return self.__precio_neto

    @property
    def cantidad(self):
        return self.__cantidad

    @precio_neto.setter
    def precio_neto(self, precio_neto):
        self.__precio_neto = precio_neto
        self.__calcular_precio_bruto()

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def __str__(self):
        return f"\n\
      Código: {self.__sku}\t \n\
      Nombre Comercial: {self.__nombre_comercial}\t \n\
      Nombre Genérico: {self.__nombre_generico}\t \n\
      Peso: {self.__peso}\t \n\
      Precio Neto: {self.__precio_neto}\t \n\
      Precio Bruto: {self.__precio_bruto}\t \n\
      Cantidad: {self.__cantidad}\t \n"""

    def __calcular_precio_bruto(self):
        self.__precio_bruto = self.__precio_neto + (self.__precio_neto * self.__impuesto)
