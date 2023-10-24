####La tienda Branko's debe vender productos a n alumnos; ofrecen:
#### Tortas, Tacos, Hot Dogs y Pizzas. Imprime la cantidad de productos vendidos en total.
from guizero import App, Box, Text, TextBox, PushButton
app = App("Tienda 'Branko'")

cantidad_personas = 0
productos_vendidos = {
    "Torta": 0,
    "Tacos": 0,
    "Hotdogs": 0,
    "Pizza": 0}
contador_comidas = 0

def registrar_venta():
    global contador_comidas
    comida = comida_box.value
    
    if comida in productos_vendidos:
        productos_vendidos[comida] += 1
        contador_comidas += 1
        resultado.value = f"Se ha vendido {contador_comidas} comida(s) en total.\n\nProductos vendidos:\n"
        for producto, cantidad in productos_vendidos.items():
            resultado.value += f"{producto}: {cantidad}\n"
        comida_box.clear()
    else:
        resultado.value = "Por favor, ingrese un producto válido (Torta, Tacos, Hotdogs o Pizza)."
def pedir_cantidad_personas():
    global cantidad_personas
    cantidad_personas = int(cantidad_personas_box.value)
    cantidad_personas_box.disable()
    resultado.value = "Ingrese el producto vendido, (Torta, Tacos, Hotdogs o Pizza)"

box = Box(app, layout="grid")
Text(box, text="Cantidad de personas a las que se les venderá:", grid=[0, 0])
cantidad_personas_box = TextBox(box, grid=[1, 0])
cantidad_personas_button = PushButton(box, text="Aceptar", command=pedir_cantidad_personas, grid=[2, 0])

Text(box, text="", grid=[0, 1])
comida_box = TextBox(box, grid=[1, 1])
registrar_button = PushButton(box, text="Registrar Venta", command=registrar_venta, grid=[2, 1])
resultado = Text(box, text="", grid=[0, 2, 3, 1])
app.display()