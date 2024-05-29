
from tkinter import *
from tkinter.ttk import *


tela1= Tk()
tela1.title("Minijogos")
tela1.geometry("380x500+500+100")
tela1.wm_resizable(width=False , height=False  )

lbl1 = Label( tela1, text='Minijogos', font= "Times 12 ").pack(side=TOP, pady=10)
#pady = quantidade de distância
photo = PhotoImage(file = r"transferir.png")
bt1 = Button(tela1,  text='Blackjack', image=photo).pack(side=LEFT)

def 


tela1.mainloop()
