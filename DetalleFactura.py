class DetalleFactura:
  def __init__(self, medicamento:Medicamento, cantidad=1):
    self.__medicamento = medicamento
    self.__cantidad = cantidad
    self.__subtotal = self.calcular_subtotal()
    self.__total = self.calcular_total()

  @property
  def subtotal(self):
    subtotal = 0
    for df in self.__total:
      subtotal += df.subtotal
    return subtotal

  def calcular_total(self):
    return (self.__medicamento.precio + self.__medicamento.valor_impuesto)*self.__cantidad

  def calcular_subtotal(self):
    return self.__medicamento.precio*self.__cantidad

  def __str__(self):
    return f"{self.medicamento}\t{self.cantidad:<8}\t{self.subtotal:<8}\t{self.total:<7}\n"