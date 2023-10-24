####na empresa desea calcular el sueldo base total de una persona bajo los siguientes rubros: sueldo base, 5% de canasta basica, 3% de prima de antiguedad y deducciones; si el salario base excede los $10,000, el impuest ISR es del 30% y si es menos que eso, sera del 20%.
#### Indique cuanto es el total de la nomina a pagar y cuantos son los impuestos que el patron debe pagar al SAT.
from guizero import App, Box, Text, TextBox, PushButton
app = App("Calcular cuanto se roban estas ratas")
cantidad_empleados: int = 0
suma_sueldos: float = 0
suma_impuestos: float = 0
contador: int = 0


def pedir_salario() -> None:
    global contador, suma_sueldos, suma_impuestos
    salario_base = float(salario_box.value)
    

    if salario_base > 10000:
        impuestos = salario_base * 0.3
    else:
        impuestos = salario_base * 0.2
    
    canasta_basica = salario_base * 0.05
    prima_antiguedad = salario_base * 0.03
    
    sueldo_total = salario_base - impuestos + canasta_basica + prima_antiguedad
    
    suma_sueldos += sueldo_total
    suma_impuestos += impuestos
    contador += 1
    
    if contador < cantidad_empleados:
        resultado.value = f"Llevamos {contador} empleado(s) calculado(s)."
    else:
        resultado.value = f"Nómina total a pagar: {suma_sueldos}\nImpuestos totales a pagar al SAT: {suma_impuestos}"

def pedir_cantidad_empleados() -> None:
    global cantidad_empleados
    cantidad_empleados = int(cantidad_empleados_box.value)
    cantidad_empleados_box.disable()
    siguiente_empleado()

def siguiente_empleado() -> None:
    salario_box.clear()
    salario_box.enable()
    calcular_button.enable()
    resultado.value = "Ingrese el salario del empleado."

box = Box(app, layout="grid")

Text(box, text="Cantidad de empleados:", grid=[0, 0])
cantidad_empleados_box = TextBox(box, grid=[1, 0])
cantidad_empleados_button = PushButton(box, text="Aceptar", command=pedir_cantidad_empleados, grid=[2, 0])

Text(box, text="", grid=[0, 1])
salario_box = TextBox(box, grid=[1, 1])
calcular_button = PushButton(box, text="Calcular Robo", command=pedir_salario, grid=[2, 1])
calcular_button.disable()
salario_box.disable()
resultado = Text(box, text="", grid=[0, 2, 2, 1])
app.display()