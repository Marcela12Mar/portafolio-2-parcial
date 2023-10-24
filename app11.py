####Captura n numeros enteros positivos, obtenga la suma de los cuadrados de los pares y el cubo de los impares
from guizero import App, Box, Text, TextBox, PushButton
app = App("Suma de Cuadrados y Cubos de Números")

n: int = 0
contador: int = 0
suma_cuadrados_pares: int = 0
suma_cubos_impares: int = 0
suma_total: int = 0 

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

def calcular_cuadrado_o_cubo() -> None:
    global contador, suma_cuadrados_pares, suma_cubos_impares
    numero = int(numero_box.value)
    
    if numero % 2 == 0:  
        cuadrado = numero ** 2
        suma_cuadrados_pares += cuadrado
    else:  
        cubo = numero ** 3
        suma_cubos_impares += cubo
    
    contador += 1
    numero_box.clear()
    siguiente_numero()

def mostrar_resultado() -> None:
    global suma_total
    suma_total = suma_cuadrados_pares + suma_cubos_impares
    resultado.value = f"La suma de los cuadrondos es: {suma_cuadrados_pares}\n"
    resultado.value += f"La suma de los cubitos es: {suma_cubos_impares}\n"
    resultado.value += f"La suma total es: {suma_total}"

box = Box(app, layout="grid")

Text(box, text="Cantidad de números a calcular:", grid=[0, 0])
cantidad_box = TextBox(box, grid=[1, 0])
cantidad_button = PushButton(box, text="TODOS WE", command=pedir_cantidad, grid=[2, 0])
text_box = Text(box, text="", grid=[0, 1])
numero_box = TextBox(box, grid=[1, 1])
calcular_button = PushButton(box, text="PIKALE AKI", command=calcular_cuadrado_o_cubo, grid=[2, 1])
calcular_button.disable()
numero_box.disable()
resultado = Text(box, text="", grid=[0, 2, 3, 1])
app.display()