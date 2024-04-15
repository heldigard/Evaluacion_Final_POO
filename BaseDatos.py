from MedicamentoVentaLibre import MedicamentoVentaLibre
from MedicamentoVentaRestringida import MedicamentoVentaRestringida


class BaseDatos:

    def __init__(self):
        pass

    def leer_inventario_desde_archivo(self, ruta) -> dict:
        inventario = {}
        with open(ruta, 'r', encoding='utf-8') as archivo:
            cabeceras = archivo.readline()

            for linea in archivo:
                vectorLinea = linea.strip().split(',')
                sku = vectorLinea[0]
                nombre_comercial = vectorLinea[1]
                nombre_generico = vectorLinea[2]
                precio_neto = vectorLinea[3]
                peso = vectorLinea[4]
                cantidad = vectorLinea[5]
                es_restringido = False if vectorLinea[6] == 'No' else True
                dosis_maxima = vectorLinea[7]
                contraindicaciones = vectorLinea[8].split(';')

                if es_restringido:
                    inventario[sku] = MedicamentoVentaRestringida(
                        sku=sku,
                        nombre_comercial=nombre_comercial,
                        nombre_generico=nombre_generico,
                        precio_neto=float(precio_neto),
                        peso=float(peso),
                        cantidad=int(cantidad),
                        es_restringido=es_restringido,
                        dosis_maxima=int(dosis_maxima),
                    )
                else:
                    inventario[sku] = MedicamentoVentaLibre(
                        sku=sku,
                        nombre_comercial=nombre_comercial,
                        nombre_generico=nombre_generico,
                        precio_neto=float(precio_neto),
                        peso=float(peso),
                        cantidad=int(cantidad),
                        es_restringido=es_restringido,
                        contraindicaciones=contraindicaciones
                    )

        return inventario
