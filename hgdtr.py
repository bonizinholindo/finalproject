from tkinter import*

root = Tk()
root.geometry("500x300+300+300" )


lbl1= Label(text="Nome" )
lbl1.place(width= 80 , height = 15, x = 10 , y =70 )
inputnome =Entry(root, font= "Time 10", show="*")
inputnome.place(width=250, height=20, x= 100 , y = 70)

lbl2= Label(text="Telefone" )
lbl2.place(width= 80 , height = 15, x = 10 , y = 110 )
inputtelefone =Entry(root, font= "Time 10", show="*")
inputtelefone.place(width=250, height=20, x= 100 , y = 110)

lbl3= Label(text="Endereço" )
lbl3.place(width= 80 , height = 15, x = 10 , y = 210 )
inputendereco =Entry(root, font= "Time 10")
inputendereco.place(width=250, height=20, x= 100 , y = 170)

lbl4= Label(text="distrito" )
lbl4.place(width= 80 , height = 15, x = 10 , y = 210 )
inputdistrito =Entry(root, font= "Time 10")
inputdistrito.place(width=250, height=20, x= 100 , y = 210)

lbl5= Label(text="País" )
lbl5.place(width= 80 , height = 15, x = 210 , y = 210 )
inputparis =Entry(root, font= "Time 10", )
inputparis.place(width=250, height=20, x= 270 , y = 210)

lbl6= Label(text="Email" )
lbl6.place(width= 80 , height = 15, x = 10 , y = 270 )
inputemail =Entry(root, font= "Time 10")
inputemail.place(width=250, height=20, x= 100 , y = 270)

btn1 = Button(text="Adicionar")
btn1.place(width= 80 , height=30 , x = 70, y= 310)

btn2 = Button(text="Pesquisar")
btn2.place(width=80 , height=30 , x=240 , y=310)


root.mainloop()









