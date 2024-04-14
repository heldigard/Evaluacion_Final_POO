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
        {self.__nombre_comercial:15}\t\
        {self.__nombre_generico:15}\t\
        {self.__peso:6}\t\
        {self.__precio_neto:6}\t\
        {self.__cantidad:6}\t\
        {self.__es_restringido:3}\t \n"


medicamento1 = Medicamento("MED001",
                           "Acetaminofén",
                           "Paracetamol",
                           "1500",
                           "10 mg",
                           "2",
                           "No")
