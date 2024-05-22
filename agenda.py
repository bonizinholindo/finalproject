



from tkinter import *
from tkinter import messagebox



tela1= Tk()
tela1.title("Agenda")
tela1.geometry("380x500+500+100")
tela1.wm_resizable(width=False , height=False  )

lb_nome = Label(tela1, text= "Nome " , font ="Time 10" , anchor="w")
lb_nome.place( width= 60 , height= 20 , x=10 , y=70)
input_nome = Entry(tela1, font= "Time 10")
input_nome.place(width=250 , height=20 , x=100 , y=70)

lb_tel = Label(tela1, text= "Telémovel " , font ="Time 10" , anchor="w")
lb_tel.place( width= 60 , height= 20 , x=10 , y=110)
input_tel = Entry(tela1, font= "Time 10")
input_tel.place(width=250 , height=20 , x=100 , y=110)



lb_end = Label(tela1, text= "Endereço " , font ="Time 10" , anchor="w")
lb_end.place( width= 60 , height= 20 , x=10 , y=170)
input_end = Entry(tela1, font= "Time 10")
input_end.place(width=250 , height=20 , x=100 , y=170)



lb_dist = Label(tela1, text= "Distrito " , font ="Time 10" , anchor="w")
lb_dist.place( width= 60 , height= 20 , x=10 , y=210)
input_dist = Entry(tela1, font= "Time 10")
input_dist.place(width=80 , height=20 , x=100 , y=210)


lb_país = Label(tela1, text= "País " , font ="Time 10" , anchor="w")
lb_país.place( width= 60 , height= 20 , x=210 , y=210)
input_país = Entry(tela1, font= "Time 10")
input_país.place(width=80 , height=20 , x=270 , y=210)


lb_email = Label(tela1, text= "Email " , font ="Time 10" , anchor="w")
lb_email.place( width= 60 , height= 20 , x=10 , y=270)
input_email = Entry(tela1, font= "Time 10")
input_email.place(width=250 , height=20 , x=100 , y=270)



def adicionar():
    nome = input_nome.get()
    tel = input_tel.get()
    end = input_end.get()
    dist = input_dist.get()
    pais = input_país.get()
    email = input_email.get()


    with open("angenda.txt" , "a") as arquivo:
        arquivo.write(nome + "\n" + tel + "\n" + end + "\n" + dist + "\n" + pais + "\n" + email + "\n")
    messagebox.showinfo("Agenda" , "Cadastro Efetuado com Sucesso!"  )
    input_nome.delete("0" , "end")
    input_tel.delete("0" , "end")
    input_end.delete("0" , "end")
    input_dist.delete("0" , "end")
    input_país.delete("0" , "end")
    input_email.delete("0" , "end")




b_adicionar = Button(tela1, text="Adicionar", command=adicionar, font = "Time 10 bold" )
b_adicionar.place( width=80 , height=30  , x=70 , y=310 )





b_procurar = Button(tela1, text="Procurar", command=adicionar, font="Time 10 bold")
b_procurar.place(width=80, height=30, x=240, y=310)




tela1.mainloop()
















































































































































































