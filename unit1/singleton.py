class ConfiguracionTienda:
    """
    Singleton: garantiza que exista una única instancia de la
    configuración general de la tienda durante toda la ejecución
    del programa.
    """

    _instancia = None

    def __new__(cls, *args, **kwargs):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia

    def __init__(self, nombre_tienda="Mi Tienda", moneda="MXN", impuestos=None):
        if self._inicializado:
            return

        self.nombre_tienda = nombre_tienda
        self.moneda = moneda
        # Tasa de impuesto por tipo de producto
        self.impuestos = impuestos or {
            "electronico": 0.16,
            "ropa": 0.08,
            "alimento": 0.00,
        }
        self._inicializado = True

    def obtener_tasa(self, tipo_producto):
        return self.impuestos.get(tipo_producto, 0.00)

    def __str__(self):
        return (
            f"ConfiguracionTienda(nombre={self.nombre_tienda!r}, "
            f"moneda={self.moneda!r}, impuestos={self.impuestos})"
        )


class Producto:
    def __init__(self, nombre, precio, tipo):
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo


class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.productos = []
        self.estado = "CREADO"
        self.config = ConfiguracionTienda()  # misma instancia siempre

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            tasa = self.config.obtener_tasa(producto.tipo)
            total += producto.precio * (1 + tasa)
        return total

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado

    def mostrar_pedido(self):
        print(f"\nPedido #{self.numero}")
        print(f"Cliente: {self.cliente}")
        print(f"Estado: {self.estado}")
        print(f"Tienda: {self.config.nombre_tienda} ({self.config.moneda})")

        print("\nProductos:")
        for producto in self.productos:
            print(f"- {producto.nombre}: ${producto.precio:.2f}")

        print(
            f"\nTotal (con impuesto): ${self.calcular_total():.2f} {self.config.moneda}"
        )


# ---------------- Programa principal ----------------
if __name__ == "__main__":
    # Demostración del Singleton
    config1 = ConfiguracionTienda(nombre_tienda="Tienda Central", moneda="MXN")
    config2 = ConfiguracionTienda()  # los argumentos aquí se ignoran

    print("¿config1 es config2?:", config1 is config2)  # True
    print(config1)
    print(config2)

    pedido = Pedido(1001, "Ana")
    pedido.agregar_producto(Producto("Laptop", 15000, "electronico"))
    pedido.agregar_producto(Producto("Playera", 500, "ropa"))
    pedido.agregar_producto(Producto("Cereal", 100, "alimento"))

    pedido.mostrar_pedido()

    pedido.cambiar_estado("ENVIADO")
    print("\nNuevo estado:", pedido.estado)

    print(
        "\n¿La configuración del pedido es la misma instancia?:",
        pedido.config is config1,
    )
