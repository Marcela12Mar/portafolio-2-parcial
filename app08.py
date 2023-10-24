####Calcule el cuadrado de un numero positivo leido del teclado.
from guizero import App, Box, Text, TextBox, PushButton
from typing import Union

app = App(title="PONI UN NUMERO")
def calcular_cuadrado() -> None:
    try:
        numero = float(input_box.value)
        if numero >= 0:
            cuadrado = numero ** 2
            resultado.value = f"El cuadrado de {numero} es {cuadrado}"
        else:
            resultado.value = "numeros positivos hijo."
    except ValueError:
        resultado.value = "ingrese un numero valido joto."

box = Box(app, layout="grid")
Text(box, text="Ingrese un número positivo:", grid=[0, 0])
input_box = TextBox(box, grid=[1, 0])
calcular_button = PushButton(box, text="Calcular Cuadrado", command=calcular_cuadrado, grid=[0, 1, 2, 1])
resultado = Text(box, text="", grid=[0, 2, 2, 1])
app.display()