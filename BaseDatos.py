from Cliente import Cliente
from MedicamentoVentaLibre import MedicamentoVentaLibre
from MedicamentoVentaRestringida import MedicamentoVentaRestringida
from Medico import Medico


def leer_inventario_desde_archivo(ruta) -> dict:
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
            contraindicaciones = vectorLinea[8].split('|')

            if es_restringido:
                inventario[sku] = MedicamentoVentaRestringida(
                    sku=sku,
                    nombre_comercial=nombre_comercial,
                    nombre_generico=nombre_generico,
                    precio_neto=float(precio_neto),
                    peso=peso,
                    cantidad_stock=int(cantidad),
                    es_restringido=es_restringido,
                    dosis_maxima=dosis_maxima,
                )
            else:
                inventario[sku] = MedicamentoVentaLibre(
                    sku=sku,
                    nombre_comercial=nombre_comercial,
                    nombre_generico=nombre_generico,
                    precio_neto=float(precio_neto),
                    peso=peso,
                    cantidad_stock=int(cantidad),
                    es_restringido=es_restringido,
                    contraindicaciones=contraindicaciones
                )

    return inventario


def leer_clientes_desde_archivo(ruta) -> dict:
    clientes = {}
    with open(ruta, 'r', encoding='utf-8') as archivo:
        cabeceras = archivo.readline()

        for linea in archivo:
            vectorLinea = linea.strip().split(',')
            cedula = vectorLinea[0]
            nombre = vectorLinea[1]
            telefono = vectorLinea[2]
            direccion = vectorLinea[3]

            clientes[cedula] = Cliente(
                nombre=nombre,
                telefono=telefono,
                cedula=cedula,
                direccion=direccion.replace('"', '')
            )

    return clientes


def leer_medicos_desde_archivo(ruta) -> list:
    medicos = []
    with open(ruta, 'r', encoding='utf-8') as archivo:
        cabeceras = archivo.readline()

        for linea in archivo:
            vectorLinea = linea.strip().split(',')
            nombre = vectorLinea[0]
            telefono = vectorLinea[1]
            especialidad = vectorLinea[2]

            medicos.append(
                Medico(
                    nombre=nombre,
                    telefono=telefono,
                    especialidad=especialidad
                )
            )

    return medicos
