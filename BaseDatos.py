from Medicamento import Medicamento


class BaseDatos:

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
                presentacion = vectorLinea[6]
                es_restringido = False if vectorLinea[7] == 'No' else True

                inventario[sku] = Medicamento(
                    sku,
                    nombre_comercial,
                    nombre_generico,
                    float(precio_neto),
                    peso,
                    int(cantidad),
                    presentacion,
                    es_restringido
                )
                pass

        return inventario




