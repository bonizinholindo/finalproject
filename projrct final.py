import tkinter as tk
import time
import random
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

tela1= Tk()
tela1.title("Minijogos")
tela1.geometry("500x500+500+100")
tela1.wm_resizable(width=False , height=False  )
vermelho = '#cc1616'

lb1 = Label(tela1, text= "MiniGames", font = "Times 18 bold")
lb1.place(width = 200 , height = 200 , x =205 , y =10 )



def blackjack():
    tela1.destroy()
    tela2 = Tk()
    tela2.title("Blackjack")
    tela2.geometry("550x400+200+200")
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
bt1.place(width=150 , height=50 , x=350 , y= 350)
#botões


# cor

#PEDRAPAPELOUTESOURA
def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate"
    elif (jogador == "Pedra" and computador == "Tesoura") or \
            (jogador == "Papel" and computador == "Pedra") or \
            (jogador == "Tesoura" and computador == "Papel"):
        return "Você venceu!"
    else:
        return "Computador venceu!"


# Função para o clique do botão
def jogar(escolha_jogador):
    escolha_computador = random.choice(["Pedra", "Papel", "Tesoura"])
    resultado = determinar_vencedor(escolha_jogador, escolha_computador)
    messagebox.showinfo("Resultado",
                        f"Você escolheu: {escolha_jogador}\nComputador escolheu: {escolha_computador}\n\n{resultado}")


def PedraPapelouTesoura():
    tela1.destroy()
    tela3 = tk.Tk()
    tela3.title("PedraPapelouTesoura")
    tela3.geometry("550x400+200+200")
    tela3.wm_resizable(width=False, height=False)


    pedra = Button(tela3, text="Pedra", width=20, command=lambda: jogar("Pedra"))
    papel = Button(tela3, text="Papel", width=20, command=lambda: jogar("Papel"))
    tesoura = Button(tela3, text="Tesoura", width=20, command=lambda: jogar("Tesoura"))


    pedra.pack(pady=10)
    papel.pack(pady=10)
    tesoura.pack(pady=10)

bt2 = Button(tela1, text='PedraPapelouTesoura', command=PedraPapelouTesoura)
bt2.place(width=150 , height=50 , x=200 , y= 350)
#botões







#PAROUIMPAR


def jogar():
    global escolha_var
    global entrada_numero


    numero_usuario = int(entrada_numero.get())
    escolha_usuario = escolha_var.get()
    try:
        numero_usuario = int(entrada_numero.get())
        if numero_usuario < 1 or numero_usuario > 10:
            raise ValueError("Número fora do intervalo permitido.")
    except ValueError as ve:
        messagebox.showerror("Erro", str(ve))
        return
    numero_computador = random.randint(1, 10)
    soma = numero_usuario + numero_computador

    resultado = "Par" if soma % 2 == 0 else "Ímpar"

    if (escolha_usuario == "Par" and resultado == "Par") or (escolha_usuario == "Ímpar" and resultado == "Ímpar"):
        mensagem = f"Você escolheu {escolha_usuario}.\nNúmero do usuário: {numero_usuario}\nNúmero do computador: {numero_computador}\nSoma: {soma} ({resultado})\nVocê ganhou!"
    else:
        mensagem = f"Você escolheu {escolha_usuario}.\nNúmero do usuário: {numero_usuario}\nNúmero do computador: {numero_computador}\nSoma: {soma} ({resultado})\nVocê perdeu!"

    messagebox.showinfo("Resultado", mensagem)


def ParouImpar():
    tela1.destroy()
    tela4 = tk.Tk()
    tela4.title("Jogo Par ou Ímpar")
    tela4.geometry("550x400+200+200")
    tela4.wm_resizable(width=False, height=False)

    global escolha_var
    global entrada_numero



    lbl = tk.Label(tela4, text="Digite um número (1-10):")
    lbl.place(x=100, y=40, width=150, height=30)
    entrada_numero = tk.Entry(tela4)
    entrada_numero.place(x=100, y=80, width=150, height=30)

    escolha_var = tk.StringVar(value="Par")
    rb_par = tk.Radiobutton(tela4, text="Par", variable=escolha_var, value="Par")
    rb_par.place(x=100, y=120)
    rb_impar = tk.Radiobutton(tela4, text="Ímpar", variable=escolha_var, value="Ímpar")
    rb_impar.place(x=160, y=120)


    btn_jogar = tk.Button(tela4, text="Jogar", command=jogar)
    btn_jogar.place(x=100, y=160, width=150, height=30)






bt3 = Button(tela1, text='ParouImpar', command=ParouImpar)
bt3.place(width=150 , height=50 , x=25 , y= 350)

















































































































































tela1.mainloop()
