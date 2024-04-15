class Medicamento:

    def __init__(
            self,
            sku,
            nombre_comercial,
            nombre_generico,
            precio_neto,
            peso,
            cantidad,
            es_restringido,
            impuesto=0.19
    ):
        self.__sku = sku
        self.__nombre_comercial = nombre_comercial
        self.__nombre_generico = nombre_generico
        self.__precio_neto = precio_neto
        self.__peso = peso
        self.__cantidad = cantidad
        self.__es_restringido = es_restringido
        self.__impuesto = impuesto

    @property
    def sku(self):
        return self.__sku

    @property
    def nombre_comercial(self):
        return self.__nombre_comercial

    @property
    def nombre_generico(self):
        return self.__nombre_generico

    @property
    def precio_neto(self):
        return self.__precio_neto

    @property
    def cantidad(self):
        return self.__cantidad

    @precio_neto.setter
    def precio_neto(self, precio_neto):
        self.__precio_neto = precio_neto

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def __str__(self):
        return f"{self.__sku:8}\t\
        {self.__nombre_comercial:25}\t\
        {self.__nombre_generico:25}\t\
        {self.__precio_neto:10}\t\t\
        {self.__peso:8}\t\
        {self.__cantidad:10}\t\t\t\
        {'SI' if self.__es_restringido else 'NO':10}\t\
        {self.__impuesto:10}\t"
