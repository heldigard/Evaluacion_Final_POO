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