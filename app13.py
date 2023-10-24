####Obtenga la suma de cinco numero capturados entre 5 y 10 inclusive
from guizero import App, Box, Text, TextBox, PushButton
app = App("Suma de los números entre 5 y 10")

contador: int = 0
suma: int = 0

def pedir_numero() -> None:
    global contador, suma
    numero = input_box.value
    try:
        numero = int(numero)
        if 5 <= numero <= 10:
            suma += numero
            contador += 1
            input_box.clear()
            if contador < 5:
                resultado.value = f"Llevamos {contador} número(s) capturado(s)."
            else:
                resultado.value = f"La suma de los 5 números es: {suma}"
                input_box.disable()
                pedir_button.disable()
        else:
            resultado.value = "Por favor, ingrese un número entre 5 y 10, inclusive."
    except ValueError:
        resultado.value = "Por favor, ingrese un número válido."


box = Box(app, layout="grid")
Text(box, text="Ingrese un número entre 5 y 10, inclusive:", grid=[0, 0])
input_box = TextBox(box, grid=[1, 0])
pedir_button = PushButton(box, text="otro numero plis", command=pedir_numero, grid=[0, 1, 2, 1])
resultado = Text(box, text="", grid=[0, 2, 2, 1])
app.display()