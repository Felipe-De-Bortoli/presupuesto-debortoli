def buscar_posicion(productos, producto):
    for i in range(len(productos)):
        if productos[i] == producto:
            return i
        
def iva (monto):
    return round(monto*0.21, 2)
def subdescuento (monto, forma_pago):
    if forma_pago == "Efectivo":
        return round(monto - monto*0.90)
    else:
        return (monto * 0)
