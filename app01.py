#### hola mundo
from guizero import App, TextBox, Text, PushButton
import pyttsx3
engine = pyttsx3.init()
app = App(title= "ICI App")
message = Text(app,text="Hola mundo" )
engine.say(f"my name is marcela")
engine.runAndWait()
app.display()