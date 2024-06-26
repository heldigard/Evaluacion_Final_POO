class Medicamento:

    def __init__(
            self,
            sku,
            nombre_comercial,
            nombre_generico,
            precio_neto,
            peso,
            cantidad_stock,
            es_restringido,
            impuesto=0.19
    ):
        self.__sku = sku
        self.__nombre_comercial = nombre_comercial
        self.__nombre_generico = nombre_generico
        self.__precio_neto = precio_neto
        self.__peso = peso
        self.__cantidad_stock = cantidad_stock
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
    def cantidad_stock(self):
        return self.__cantidad_stock

    @property
    def impuesto(self):
        return self.__impuesto

    @property
    def peso(self):
        return self.__peso

    @property
    def es_restringido(self):
        return self.__es_restringido

    @precio_neto.setter
    def precio_neto(self, precio_neto):
        self.__precio_neto = precio_neto

    @cantidad_stock.setter
    def cantidad_stock(self, cantidad_stock):
        self.__cantidad_stock = cantidad_stock

    def __str__(self):
        return f"{self.__sku:8}\t\
        {self.__nombre_comercial:20}\t\
        {self.__nombre_generico:20}\t\
        {self.__precio_neto:10}\t\t\
        {self.__peso:8}\t\
        {self.__cantidad_stock:10}\t\t\t\
        {'SI' if self.__es_restringido else 'NO':10}\t\
        {self.__impuesto:10}\t"
