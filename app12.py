####Dado el año de nacimiento, indique cuantos años va a cumplir el siguiente año.
from guizero import App, Box, Text, TextBox, PushButton
app = App("Calculador de que tan viejo estas")

def calcular_edad() -> None:
    try:
        anio_nacimiento = int(input_box.value)
        anio_actual = 2023 
        if anio_nacimiento > 0 and anio_nacimiento <= anio_actual:
            edad = anio_actual - anio_nacimiento
            resultado.value = f"Usted va a cumplir {edad+1} años pal año que entra."
        else:
            resultado.value = "Por favor, ingrese un año de nacimiento válido."
    except ValueError:
        resultado.value = "Por favor, ingrese un año de nacimiento válido."

box = Box(app, layout="grid")
Text(box, text="Ingrese su año de nacimiento:", grid=[0, 0])
input_box = TextBox(box, grid=[1, 0])
calcular_button = PushButton(box, text="Calcular Edad", command=calcular_edad, grid=[0, 1, 2, 1])
resultado = Text(box, text="", grid=[0, 2, 2, 1])
app.display()