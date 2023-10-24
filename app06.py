####Obtener la edad promedio de n personas preguntando su año de nacimiento y asumiendo que el año actual es 2023.
from guizero import App, Box, Text, TextBox, PushButton, ListBox
app = App(title="Los espermatozoides ganadores", width=20, height=20)
años_parto = []
porcion_personas = 0

def calcular_edad_promedio():
    try:
        if cantidad_personas == len(años_parto):
            edades = [2023 - int(año) for año in años_parto]
            edad_promedio = sum(edades) / len(edades)
            resultado.value = f"Edad promedio: {edad_promedio:.2f} años"
        else:
            resultado.value = "Ingrese el año de nacimiento de todas las personas."
    except ValueError:
        resultado.value = "Ingrese años de nacimiento válidos."

def agregar_año():
    try:
        año = int(entrada_año.value)
        if año <= 2023:
            años_parto.append(entrada_año.value)
            lista_años.append(entrada_año.value)
            entrada_año.clear()
            if len(años_parto) == cantidad_personas:
                agregar_button.disable()
        else:
            entrada_año.clear()
    except ValueError:
        entrada_año.clear()

def configurar_cantidad():
    global cantidad_personas
    try:
        cantidad_personas = int(cantidad_personas_input.value)
        if cantidad_personas > 0:
            cantidad_personas_input.disable()
            configurar_button.disable()
            entrada_año.enable()
            agregar_button.enable()
            calcular_button.enable()
        else:
            cantidad_personas_input.clear()
    except ValueError:
        cantidad_personas_input.clear()

box = Box(app, layout="grid")
Text(box, text="Ingrese la cantidad de personas:", grid=[0, 0, 2, 1])
cantidad_personas_input = TextBox(box, grid=[2, 0])
configurar_button = PushButton(box, configurar_cantidad, text="Configurar", grid=[3, 0])
Text(box, text="Ingrese el año de nacimiento:", grid=[0, 1])
entrada_año = TextBox(box, grid=[1, 1])
agregar_button = PushButton(box, agregar_año, text="Agregar", grid=[2, 1])
lista_años = ListBox(box, items=[], grid=[0, 2, 3, 3])
calcular_button = PushButton(box, calcular_edad_promedio, text="Calcular Edad Promedio", grid=[0, 5, 3, 1])
resultado = Text(box, text="", grid=[0, 6, 3, 1])
app.display()