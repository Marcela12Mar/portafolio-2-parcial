#### Calcular el promedio de n numeros positivos leidos del teclado 
from guizero import App, Box, PushButton, TextBox, Text
app = App(title= "Promedio de n números:D")
can_numeros = 0
numerukis = []

def calcular_promedio():
    global can_numeros
    numerukis.clear()
    can_numeros = int(input_cantidad_numeros.value)

    for i in range(can_numeros):
        numero = float(input_numeros[i].value)
        numerukis.append(numero)

    if len(numerukis) > 0:
        promedio = sum(numerukis) / len(numerukis)
        resultado.value = "El promedio es: {:.2f}".format(promedio)
    else:
        resultado.value = "No se ingresaron números válidos."

def preguntar_cantidad():
    cantidad_numeros = int(input_cantidad_numeros.value)
    input_numeros.clear()
    for i in range(cantidad_numeros):
        Text(box, text="Número {}: ".format(i + 1), grid=[0, i + 1])
        input_numeros.append(TextBox(box, grid=[1, i + 1]))
    calcular_button.enabled = True

box = Box(app, layout="grid")
Text(box, text="cantidad de teletubies:", grid=[0, 0])
input_cantidad_numeros = TextBox(box, grid=[1, 0])
calcular_button = PushButton(box, text="Calcular", command=calcular_promedio, grid=[2, 0])
calcular_button.enabled = False

preguntar_button = PushButton(box, text="Preguntar teletubies", command=preguntar_cantidad, grid=[2, 1])
input_numeros = []
resultado = Text(box, text="", grid=[0, 12, 2, 1])

app.display()



