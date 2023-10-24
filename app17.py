####Preguntar un numero y asumir que dia de la semana es.
#Determinar que día de la semana es, preguntando un numero

from guizero import App, Box, Text, TextBox, PushButton
app = App("que dia son los de pistear")
def determinar_dia_semana():
    try:
        numero = int(numero_box.value) 
        if 1 <= numero <= 7:  
            dias_semana = ["Lunetas", "Martesini", "Miércoles", "Jueveson", "Viernukis", "Sábadukis", "Domingo"]
            dia_semana = dias_semana[numero - 1]  
            resultado.value = f"El número {numero} corresponde a {dia_semana}."
        else:
            resultado.value = "Por favor, ingrese un número entre 1 y 7."
    except ValueError:
        resultado.value = "Por favor, ingrese un número válido."

app = App("Determinar Día de la Semana")
box = Box(app, layout="grid")
Text(box, text="Ingrese un número del 1 al 7:", grid=[0, 0])
numero_box = TextBox(box, grid=[1, 0])
determinar_button = PushButton(box, text="Determinar Día de la Semana", command=determinar_dia_semana, grid=[0, 1, 2, 1])
resultado = Text(box, text="", grid=[0, 2, 2, 1])
app.display()