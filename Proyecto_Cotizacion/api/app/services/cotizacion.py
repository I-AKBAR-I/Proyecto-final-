class Cotizacion:
    def __init__(self, cliente, ventanas):
        self.cliente = cliente
        self.ventanas = ventanas

    def calcular_total(self):
        total = sum([ventana['alto'] * ventana['ancho'] * ventana['precio'] for ventana in self.ventanas])
        return total
