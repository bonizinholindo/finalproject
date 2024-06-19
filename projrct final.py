
import time
import random
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

tela1= Tk()
tela1.title("Minijogos")
tela1.geometry("380x500+500+100")
tela1.wm_resizable(width=False , height=False  )




def blackjack():
    tela1.destroy()
    tela2 = Tk()
    tela2.title("Blackjack")
    tela2.geometry("380x500+500+100")
    tela2.wm_resizable(width=False, height=False)
    vermelho = '#cc1616'



    lb_scorep = Label(tela2, text='Score Player:', font='Times 18 bold')
    lb_scorep.place(width=140, height=40, x=5, y=5)
    lb_player = Label(tela2, text='0', font=('Times 18 bold'))
    lb_player.place(width=20, height=40, x=150, y=5)

    lb_scorec = Label(tela2, text='Score Cassino:', font=('Times 18 bold'))
    lb_scorec.place(width=150, height=40, x=360, y=5)
    lb_cassino = Label(tela2, text='0', font=('Times 18 bold'))
    lb_cassino.place(width=20, height=40, x=520, y=5)
    lb_resultado = Label(tela2, text='Iniciar jogo', font=('Times 24'))
    lb_resultado.place(width=200, height=100, x=300, y=200)

    lb_soma = Label(tela2, font=('Times 40 bold'))
    lb_soma.place(width=50, height=50, x=150, y=90)

    lb_carta = Label(tela2, font=('Times 24'))
    lb_carta.place(width=50, height=50, x=35, y=200)

    lb_banca = Label(tela2, font=('Times 40 bold'))
    lb_banca.place(width=50, height=50, x=380, y=90)
    b_novo = Button(tela2, text='Novo', command=novo)
    b_novo.place(width=75, height=40, x=450, y=350)



def comprar():
        global somatorio
        global pt_cpu
        global lb_soma
        global lb_carta
        cartas = random.randint(2, 10)
        lb_carta.configure(text=cartas)
        somatorio += cartas
        lb_soma.configure(text=somatorio)

        if somatorio > 21:
            b_jogar.destroy()
            b_passar.destroy()
            pt_cpu += 1
            lb_cassino.configure(text=pt_cpu)
            lb_resultado.configure(text='Você perdeu')

def novo():
        global b_jogar
        global b_passar
        global somatorio
        global pt_player
        global pt_cpu

        somatorio = 0

        lb_resultado.configure(text='Em jogo ..')
        lb_soma.configure(text=' ')
        lb_carta.configure(text=' ')
        lb_banca.configure(text=' ')

        b_jogar = Button(tela1, text='Comprar', command=comprar, font=('Times 20 bold'))
        b_jogar.place(width=150, height=50, x=100, y=200)

        b_passar = Button(tela1, text='Deitar', command=passar, font=('Times 20 bold'))
        b_passar.place(width=150, height=50, x=100, y=275)



def passar():
    global pt_player
    global pt_cpu
    global lb_banca
    global lb_cassino
    global lb_resultado
    global lb_player

    cartas2 = random.randint(14, 21)
    lb_banca.configure(text=cartas2)

    b_jogar.destroy()
    b_passar.destroy()

    if somatorio > cartas2:
        pt_player += 1
        lb_player.configure(text=pt_player)
        lb_resultado.configure(text='Ganhou!')
    elif somatorio == cartas2:
        lb_resultado.configure(text='Empate')
    else:
        pt_cpu += 1
        lb_cassino.configure(text=pt_cpu)
        lb_resultado.configure(text='Perdeu!')

    vermelho = '#cc1616'

    b_novo = Button(tela1, text='Novo', command=novo)
    b_novo.place(width=75, height=40, x=450, y=350)

lbl1 = Label(tela1, text='Minijogos', font="Times 12 ")
bt1 = Button(tela1, text='blackjack', command=blackjack)
bt1.place(width=80 , height=30 , x=230 , y= 140)
#botões


# cor
vermelho = '#cc1616'
# cor

#funços



#Par ou Impar



import tkinter as tk
from tkinter import messagebox
import random

def play_game():
    user_choice = choice.get()
    user_number = number_entry.get()

    if user_choice not in ["Par", "Ímpar"]:
        messagebox.showwarning("Erro", "Por favor, escolha Par ou Ímpar.")
        return

    try:
        user_number = int(user_number)
    except ValueError:
        messagebox.showwarning("Erro", "Por favor, insira um número válido.")
        return

    computer_number = random.randint(0, 10)
    total = user_number + computer_number

    result = "Par" if total % 2 == 0 else "Ímpar"
    result_message = f"Você escolheu: {user_choice}\nSeu número: {user_number}\nNúmero do computador: {computer_number}\nTotal: {total} ({result})"

    if result == user_choice:
        result_message += "\n\nVocê venceu!"
    else:
        result_message += "\n\nVocê perdeu!"

    messagebox.showinfo("Resultado", result_message)

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Jogo Par ou Ímpar")

# Label para escolher Par ou Ímpar
choice_label = tk.Label(root, text="Escolha Par ou Ímpar:", font=('Helvetica', 14))
choice_label.pack(pady=10)

# Botões para escolher Par ou Ímpar
choice = tk.StringVar()
par_button = tk.Radiobutton(root, text="Par", variable=choice, value="Par", font=('Helvetica', 14))
par_button.pack(pady=5)
impar_button = tk.Radiobutton(root, text="Ímpar", variable=choice, value="Ímpar", font=('Helvetica', 14))
impar_button.pack(pady=5)

# Label para inserir um número
number_label = tk.Label(root, text="Insira um número:", font=('Helvetica', 14))
number_label.pack(pady=10)

# Entrada para inserir um número
number_entry = tk.Entry(root, font=('Helvetica', 14))
number_entry.pack(pady=10)

# Botão para jogar
play_button = tk.Button(root, text="Jogar", command=play_game, font=('Helvetica', 14))
play_button.pack(pady=20)

# Executa a interface Tkinter
root.mainloop()




























































































































































































tela1.mainloop()
