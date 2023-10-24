####Obtener la suma de todos los cuadrados de los numeros pares entre 0 y 20 consecutivos
from guizero import App, Box, Text, PushButton
app = App("Suma de Cuadrados de Números Pares")

def calcular_suma_cuadrados() -> None:
    contador = 0
    suma_cuadrados = 0
    
    while contador < 10:
        numero = contador * 2
        cuadrado = numero ** 2
        suma_cuadrados += cuadrado
        contador += 1

    resultado.value = f"La suma de los cuadrados de los números pares entre 0 y 20 es: {suma_cuadrados}"

app = App("Suma de Cuadrados de Números Pares")
box = Box(app, layout="grid")
calcular_button = PushButton(box, text="Calcular Suma de Cuadrados", command=calcular_suma_cuadrados, grid=[0, 0, 2, 1])
resultado = Text(box, text="", grid=[0, 1, 2, 1])
app.display()