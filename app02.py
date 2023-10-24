#### promedio de tres numeros capturados
from guizero import App, TextBox, Text, PushButton
app = App(title= "Promedio de tres  numeros capturados :D")
num1 = 30
num2 = 20
num3 = 10

def capturar_numeros():
    global num1, num2, num3
    num1= float(input.num1.value)
    num2 = float(input.num2.value)
    num3 = float(input.num3.value)
message = Text(app,text="Dame el primer numero",)
name = TextBox(app, width=50,height=50)
message = Text(app,text="Dame el segundo numero",)
name = TextBox(app, width=50,height=50)
message = Text(app,text="Dame el tercer numero",)
name = TextBox(app, width=50,height=50)

def calcular_promedio():
    promedio = (num1 + num2 + num3) / 3
    app.info(title="resultado", text= f"el promedio capturado es: {promedio}")
button = PushButton(app, text="pikale aki", command= calcular_promedio)

app.display()
