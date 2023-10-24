####btener la suma de todos los cuadrados de n numeros capturados del teclado
from guizero import App, Box, Text, TextBox, PushButton
app = App("Suma de CUADRADITOS")

n: int = 0
contador: int = 0
suma_cuadrados: float = 0.0

def pedir_cantidad() -> None:
    global n
    n = int(cantidad_box.value)
    cantidad_box.disable()
    siguiente_numero()

def siguiente_numero() -> None:
    global contador
    if contador < n:
        text_box.value = f"Ingrese el número {contador + 1}:"
        numero_box.enable()
        calcular_button.enable()
    else:
        mostrar_resultado()

def calcular_cuadrado() -> None:
    global contador, suma_cuadrados
    numero = float(numero_box.value)
    if numero >= 0:
        cuadrado = numero ** 2
        suma_cuadrados += cuadrado
        contador += 1
        numero_box.clear()
        siguiente_numero()
    else:
        text_box.value = "Por favor, ingrese un número positivo."

def mostrar_resultado() -> None:
    resultado.value = f"La suma de los cuadrados de los {n} números es: {suma_cuadrados:.2f}"



box = Box(app, layout="grid")
Text(box, text="Cantidad de números a calcular:", grid=[0, 0])
cantidad_box = TextBox(box, grid=[1, 0])
cantidad_button = PushButton(box, text="Aceptar", command=pedir_cantidad, grid=[2, 0])
text_box = Text(box, text="", grid=[0, 1])
numero_box = TextBox(box, grid=[1, 1])
calcular_button = PushButton(box, text="Calcular", command=calcular_cuadrado, grid=[2, 1])
calcular_button.disable()
numero_box.disable()
resultado = Text(box, text="", grid=[0, 2, 3, 1])
app.display()