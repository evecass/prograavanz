from .utilidades import (
    _obtener_fecha_actual,
    formatear_encabezado
)

def crear_reporte_ventas(monto):
    encabezado = formatear_encabezado("REPORTE DE VENTAS")
    fecha = _obtener_fecha_actual()

    reporte = (
        f"{encabezado}\n"
        f"Fecha: {fecha}\n"
        f"Monto total abonado: ${monto:,.2f}"
    )

    return reporte

def crear_reporte_inventario(items):
    cantidad = len(items)

    reporte = (
        f"REPORTE DE INVENTARIO\n"
        f"Cantidad total de artículos: {cantidad}"
    )

    return reporte
