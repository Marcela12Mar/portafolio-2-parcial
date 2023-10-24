####Obtener la edad de una persona preguntando el año actual y el año de nacimiento.
from guizero import App, TextBox, Text, PushButton
import pyttsx3
engine = pyttsx3.init()

app = App(title= "TU EDAD")
a_actual= int
a_nacimiento:int  
def calcular_edad():
    global a_actual, a_nacimiento, cadena
    cadena = ''
    a_nacimiento = 0
    a_actual=0
    a_actual = int(name.value)
    a_nacimiento = int(name2.value)
    años = (a_actual - a_nacimiento)
    engine.say(cadena)
    app.info(title="edad", text= f"tu edad es: {años}")
    cadena = f"tu edad es: {años}"
 
 
   
message = Text(app,text="¿Cuál es el año actual?")
name = TextBox(app, width=20,height=20)
message = Text(app,text="¿Cuál es tu fecha de cumple años?")
name2 = TextBox(app, width=20,height=20)
button = PushButton(app, text="PIKALE", command= calcular_edad)
engine.say(f"¿Cuál es el año actual?")
engine.runAndWait()
engine.say(f"¿cual es tu fecha de cumpleaños?")
engine.runAndWait()

app.display()