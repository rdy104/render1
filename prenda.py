class Prenda:
    DESCUENTO_OFERTA = 0.20
 
    def __init__(self, nombre, precio, categoria, talla, stock, fecha_ingreso, en_oferta=False):
        self.nombre = nombre
        self.precio = precio            # pasa por el setter: se valida desde el inicio
        self.categoria = categoria
        self.talla = talla
        self.stock = stock
        self.fecha_ingreso = fecha_ingreso
        self.en_oferta = en_oferta
 
    @property
    def precio(self):
        return self.__precio
 
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self.__precio = nuevo_precio
 
    def precio_final(self):
        if self.en_oferta:
            return self.precio * (1 - self.DESCUENTO_OFERTA)
        return self.precio
 
    def valor_stock(self):
        return self.precio_final() * self.stock
 
    def __str__(self):
        etiqueta = " (oferta)" if self.en_oferta else ""
        return f"{self.nombre} [{self.categoria}, {self.talla}] - Bs {self.precio_final():.2f}{etiqueta}"
