from tkinter import*
import requests
from PIL import ImageTk
from urllib.request import urlopen


apikey = "aba304e1b88c4bbeff3e1524ea015a8b"


tela = Tk()

weatherget = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang=pt_br")
weather = weatherget.json()

iconcode = weather ["weather"] [0] ["icon"]
icone = str(iconcode+"@4x.png")
urlimage = ("http://")













