import pygame
import time
import random
from tkinter import *
from tkinter.ttk import *


tela1= Tk()
tela1.title("Minijogos")
tela1.geometry("380x500+500+100")
tela1.wm_resizable(width=False , height=False  )

lbl1 = Label( tela1, text='Minijogos', font= "Times 12 ").pack(side=TOP, pady=10)
#pady = quantidade de distância

def blackjack():
    photo = PhotoImage(file=r"transferir.png")
    bt1 = Button(tela1, text='Blackjack',command= blackjack , image=photo).pack(side=LEFT)






def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 5)

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas, colunas e diagonais
    for linha in tabuleiro:
        if all([celula == jogador for celula in linha]):
            return True
    for coluna in range(3):
        if all([tabuleiro[linha][coluna] == jogador for linha in range(3)]):
            return True
    if all([tabuleiro[i][i] == jogador for i in range(3)]) or all([tabuleiro[i][2-i] == jogador for i in range(3)]):
        return True
    return False

def jogo_da_velha():
    photo = PhotoImage(file=r"transferir.png")
    bt2 = Button(tela1, text="Jogo Da Velha", command=jogo_da_velha(), image=photo).pack(side=RIGHT)

    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

    jogador = "X"

    for _ in range(9):
        exibir_tabuleiro(tabuleiro)
        linha, coluna = map(int, input(f'Jogador {jogador}, escolha linha e coluna (0, 1 ou 2): ').split())
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador
            if verificar_vitoria(tabuleiro, jogador):
                exibir_tabuleiro(tabuleiro)
                print(f'Jogador {jogador} venceu!')
                return
            jogador = "O" if jogador == "X" else "X"
        else:
            print("Celula ocupada, tente novamente.")

    exibir_tabuleiro(tabuleiro)
    print("Empate!")

jogo_da_velha()

































































































































































































tela1.mainloop()
