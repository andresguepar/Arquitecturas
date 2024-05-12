class Product:
    def __init__(self, id, name, stock):
        self.id = id
        self.nombre = name
        self.stock = stock

class Inventory:

    def __init__(self):
        self.products = []

    def add(self, name, stock):
        id = len(self.products) + 1
        new_product = Product(id, name, stock)
        self.products.append(new_product)

    def sell(self, id, stock):
       
        for product in self.products:
            if product.id == id:
                if product.stock >= stock:
                    product.stock -= stock
                    print(f"Se vendieron {stock} unidades de {product.nombre}.")
                else:
                    print("No hay suficientes unidades en el inventario.")
                return
        print("El producto no está en el inventario.")

    def show(self):
        print("Inventario:")
        for product in self.products:
            print(f"{product.nombre}: {product.stock} unidades")


inventory = Inventory()

inventory.add("Celular", 50)
inventory.add("Tablet", 30)
inventory.add("Audifonos", 20)

inventory.sell(1, 10) 

inventory.show()
