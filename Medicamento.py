class Medicamento:

    def __init__(
            self,
            codigo,
            nombre_comercial,
            nombre_generico,
            peso,
            cantidad,
            sin_impuesto,
            impuesto=0.19
    ):
        self.__codigo = codigo
        self.__nombre_comercial = nombre_comercial
        self.__nombre_generico = nombre_generico
        self.__peso = peso
        self.__cantidad = cantidad
        self.__sin_impuesto = sin_impuesto
        self.__impuesto = impuesto

    def __str__(self):
        return f"\n\
      Código: {self.__codigo}\t \n\
      Nombre comercial: {self.__nombre_comercial}\t \n\
      Nombre genérico: {self.__nombre_generico}\t \n\
      Peso: {self.__peso}"
