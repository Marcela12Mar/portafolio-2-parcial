#### Obtener el promedio de dos numeros positivos leidos del teclado.
from guizero import App, TextBox, Text, PushButton


app = App(title= "PROMEDIO")
def calcular_promedio():
    global n1, n2
    n1 = 0
    n2= 0
    n1 = int(name.value)
    n2 = int(name2.value)
    promedio = (n1 + n2) / 2
    app.info(title="promedio de dos numeros", text= f"el promedio es: {promedio}")
button = PushButton(app, text="PIKALE", command= calcular_promedio)

message = Text(app,text="Dame el primer numero para sumar ")
name = TextBox(app, width=20,height=20)
message = Text(app,text="Dame el segundo numero para sumar")
name2 = TextBox(app, width=20,height=20)
app.display()