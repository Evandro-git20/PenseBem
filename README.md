from tkinter import *

def ct(op1):
    if(op1 == 1):
        bt5 = Button(janela, text="Responder", bg="green", foreground="white", command=ct5)
        bt5.place(x=10, y=260)

def ct2(op2):
    if(op2 == 2):
        bt5 = Button(janela, text="Responder", bg="green", foreground="white", command=ct6)
        bt5.place(x=10, y=260)

def ct3(op3):
    if(op3 == 3):
        bt5 = Button(janela, text="Responder", bg="green", foreground="white", command=ct7)
        bt5.place(x=10, y=260)

def ct4(op4):
    if(op4 == 4):
        bt5 = Button(janela, text="Responder", bg="green", foreground="white", command=ct8)
        bt5.place(x=10, y=260)

def ct5():
        bt1["foreground"] = "green"
        bt7 = Button(janela, width=8, text="Próxima", bg="blue", foreground="white", command=qt2)
        bt7.place(x=87, y=260)
        bt8 = Button(janela, text="Comentário", bg="yellow", foreground="black", command=ct8)
        bt8.place(x=10, y=260)

def ct6():
    bt2["foreground"] = "red"
    bt7 = Button(janela, width=8, text="Próxima", bg="blue", foreground="white", command=qt2)
    bt7.place(x=87, y=260)
    bt8 = Button(janela, text="Comentário", bg="yellow", foreground="black", command=ct8)
    bt8.place(x=10, y=260)

def ct7():
    bt3["foreground"] = "red"
    bt7 = Button(janela, width=8, text="Próxima", bg="blue", foreground="white", command=qt2)
    bt7.place(x=87, y=260)
    bt8 = Button(janela, text="Comentário", bg="yellow", foreground="black", command=ct8)
    bt8.place(x=10, y=260)

def ct8():
    bt4["foreground"] = "red"
    bt7 = Button(janela, width=8, text="Próxima", bg="blue", foreground="white", command=qt2)
    bt7.place(x=87, y=260)
    bt8 = Button(janela, text="Comentário", bg="yellow", foreground="black", command=ct8)
    bt8.place(x=10, y=260)

def qt2():
    lb1["text"] = "QUESTÃO 2"
    lb1["text"] = "Você tem algum        no trabalho?"

janela = Tk()

lb1 = Label(janela, text="QUESTÃO 1", font="verdana", bg="white").pack()
lb2 = Label(janela, text="Você tem algum        comigo?", font="verdana", bg="white").pack()

i = IntVar()
bt1 = Radiobutton(janela, width=10, bg="white", text= "Problema", command=lambda:ct(1), variable=i, value=1)
bt1.place(x=10, y=70)
bt2 = Radiobutton(janela, width=10, bg="white", text= "probrema", command=lambda:ct2(2), variable=i, value=2)
bt2.place(x=10, y=100)
bt3 = Radiobutton(janela, width=10, bg="white", text= "poblema", command=lambda:ct3(3), variable=i, value=3)
bt3.place(x=8, y=130)
bt4 = Radiobutton(janela, width=10, bg="white", text= "pobrema", command=lambda:ct4(4), variable=i, value=4)
bt4.place(x=8, y=165)
bt6 = Button(janela, text="X", bg="red", foreground="white")
bt6.place(x=270, y=260)

janela.title("Escreva Bem")
janela.configure(bg='white')
janela.geometry("300x300+200+200")
janela.mainloop()
