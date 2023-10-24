####Se desea saber la cantidad de alumnos que pasaron una materia. Son 25 y la calificación aprobatoria es 7
from guizero import App, Box, TextBox, PushButton, Text

app = App(title=" Alumnos no Pdjs", width=300, height=300)

def saber_aprobacion(calificacion):
    calificacion = int(calificacion)
    if calificacion >= 7:
        return True
    else:
        return False


def contar_aprobados():
    calificaciones = [entrada_calificaciones[i].value for i in range(25)]
    aprobados = sum(saber_aprobacion(cal) for cal in calificaciones)
    resultado.value = f"Alumnos que si le saben: {aprobados}"

Box(app, layout="grid")
entrada_calificaciones = [TextBox(Box, text="Calificación:") for _ in range(25)]
boton_verificar = PushButton(Box, text="Verificar", command=contar_aprobados)
resultado = Text(Box, text="", grid=[0, 27])

app.display()