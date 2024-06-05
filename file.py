from tkinter import *
from random import randint
# -------------------------------------------------------------
# cor
vermelho = '#cc1616'
# cor
pt_player = 0
pt_cpu = 0
# -------------------------------------------------------------
# tela
tela1 = Tk()
tela1.title('21 Card Game')
tela1.geometry('550x400+200+200')
tela1.wm_resizable(width=False, height=False)
# -------------------------------------------------------------

#funços

def comprar():
    global somatorio
    global pt_cpu

    cartas = randint(2, 10)
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

    cartas2 = randint(14, 21)
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


#labels
lb_scorep = Label(tela1, text='Score Player:', font=('Times 18 bold'))
lb_scorep.place(width=140, height=40, x=5, y=5)
lb_player = Label(tela1, text='0', font=('Times 18 bold'))
lb_player.place(width=20, height=40, x=150, y=5)

lb_scorec = Label(tela1, text='Score Cassino:', font=('Times 18 bold'))
lb_scorec.place(width=150, height=40, x=360, y=5)
lb_cassino = Label(tela1, text='0', font=('Times 18 bold'))
lb_cassino.place(width=20, height=40, x=520, y=5)
lb_resultado = Label(tela1, text='Iniciar jogo', font=('Times 24'))
lb_resultado.place(width=200, height=100, x=300, y=200)

lb_soma = Label(tela1, font=('Times 40 bold'), fg=vermelho)
lb_soma.place(width=50, height=50, x=150, y=90)

lb_carta = Label(tela1, font=('Times 24'))
lb_carta.place(width=50, height=50, x=35, y=200)

lb_banca = Label(tela1, font=('Times 40 bold'), fg=vermelho)
lb_banca.place(width=50, height=50, x=380, y=90)
#labels
#botões
b_novo=Button(tela1, text='Novo', command=novo, font='Stencil 15 bold')
b_novo.place(width=75, height=40, x=450, y=350)
#botões
tela1.mainloop()