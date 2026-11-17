# Importamos la clase Pedido desde el módulo modelos (el archivo modelos.py)
from modelos import Pedido

# Creamos objetos de la clase con datos de prueba
pedido1 = Pedido("Ana", "Teclado mecánico", 1, 899.00)
pedido2 = Pedido("Luis", "Mouse inalámbrico", 2, 349.50)

# Imprimimos el resultado del método de la clase
print(pedido1.resumen())
print(pedido2.resumen())
