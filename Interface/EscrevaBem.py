from tkinter import *
import pygame

pygame.init()

janela = Tk()
janela.title("ESCREVA BEM")
janela.configure(bg='#f2f2f2')
janela.geometry("800x600")

fundo = PhotoImage(file='imagens/fundo2.png')
Label(janela, image=fundo).place(relwidth=1, relheight=1)

questao_correta = 0
questao_errada = 0


class Operacao:
    def __init__(self, op):
        op = self.op

    def ct(op1):
        if op1 == 1:
            bt5 = Button(janela,
                         text="Responder",
                         width=10,
                         font=('Verdana', 15),
                         bg="green",
                         foreground="#f2f2f2",
                         command=ct5)
            bt5.place(x=322, y=520)

        def ct2(op2):
            if op2 == 2:
                bt5 = Button(janela,
                             text="Responder",
                             width=10,
                             font=('Verdana', 15),
                             bg="green",
                             foreground="#f2f2f2",
                             command=ct6)
                bt5.place(x=322, y=520)

        def ct3(op3):
            if op3 == 3:
                bt5 = Button(janela,
                             text="Responder",
                             width=10,
                             font=('Verdana', 15),
                             bg="green",
                             foreground="#f2f2f2",
                             command=ct7)
                bt5.place(x=322, y=520)

        def ct4(op4):
            if op4 == 4:
                bt5 = Button(janela,
                             text="Responder",
                             width=10,
                             font=('Verdana', 15),
                             bg="green",
                             foreground="#f2f2f2",
                             command=ct8)
                bt5.place(x=322, y=520)

        def ct5():
            bt1["foreground"] = "green"
            pygame.mixer.music.load('sons/correto.wav')
            pygame.mixer.music.play(1)
            bt2.destroy()
            bt3.destroy()
            bt4.destroy()
            bt7 = Button(janela, width=10,
                         text="PRÓXIMA",
                         bg="blue",
                         font=('Verdana', 10),
                         foreground="#f2f2f2",
                         command=qt2)
            bt7.place(x=20, y=550)

        def ct6():
            bt2["foreground"] = "red"
            pygame.mixer.music.load('sons/errado.wav')
            pygame.mixer.music.play()
            bt1.destroy()
            bt3.destroy()
            bt4.destroy()
            bt7 = Button(janela, width=10,
                         text="PRÓXIMA",
                         bg="blue",
                         font=('Verdana', 10),
                         foreground="#f2f2f2",
                         command=qt2)
            bt7.place(x=200, y=550)
            bt8 = Button(janela,
                         width=20,
                         text="COMENTÁRIO",
                         bg="yellow",
                         font=('Verdana', 10),
                         foreground="black",
                         command=q1erro)
            bt8.place(x=20, y=550)

        def ct7():
            bt3["foreground"] = "red"
            pygame.mixer.music.load('sons/errado.wav')
            pygame.mixer.music.play()
            bt1.destroy()
            bt2.destroy()
            bt4.destroy()
            bt7 = Button(janela, width=10,
                         text="PRÓXIMA",
                         bg="blue",
                         font=('Verdana', 10),
                         foreground="#f2f2f2",
                         command=qt2)
            bt7.place(x=200, y=550)
            bt8 = Button(janela,
                         width=20,
                         text="COMENTÁRIO",
                         bg="yellow",
                         font=('Verdana', 10),
                         foreground="black",
                         command=q1erro)
            bt8.place(x=20, y=550)

        def ct8():
            bt4["foreground"] = "red"
            pygame.mixer.music.load('sons/errado.wav')
            pygame.mixer.music.play()
            bt1.destroy()
            bt2.destroy()
            bt3.destroy()
            bt7 = Button(janela, width=10,
                         text="PRÓXIMA",
                         bg="blue",
                         font=('Verdana', 10),
                         foreground="#f2f2f2",
                         command=qt2)
            bt7.place(x=20, y=330)
            bt8 = Button(janela,
                         width=20,
                         text="COMENTÁRIO",
                         bg="yellow",
                         font=('Verdana', 10),
                         foreground="black",
                         command=q1erro)
            bt8.place(x=20, y=550)


# QUESTAO 1


lb1 = Label(janela, text="QUESTÃO 1", font=("verdana", 30), bg='#262626', fg='white')
lb1.place(x=280, y=15)
lb2 = Label(janela, text="Você tem algum ... comigo?", font=("verdana", 25), bg='#262626', fg='white')
lb2.place(x=150, y=110)

i = IntVar()
bt1 = Radiobutton(janela, bg='#262626', fg='#b38f00', indicatoron=0, activebackground='#cccccc',
                  activeforeground='black', text="PROBLEMA", width=30, font=('Arial', 20), pady=3, padx=5,
                  command=lambda: ct(1), variable=i, value=1)
bt1.place(x=150, y=250)

bt2 = Radiobutton(janela, bg='#262626', fg='#b38f00', indicatoron=0, text="PROBREMA", width=30, font=('Arial', 20),
                  pady=3, padx=5, command=lambda: ct2(2), variable=i, value=2)
bt2.place(x=150, y=310)

bt3 = Radiobutton(janela, bg='#262626', fg='#b38f00',
                  indicatoron=0,
                  text="POBLEMA", width=30, font=('Arial', 20), pady=3, padx=5, command=lambda: ct3(3), variable=i,
                  value=3)
bt3.place(x=150, y=370)

bt4 = Radiobutton(janela, bg='#262626', fg='#b38f00',
                  indicatoron=0,
                  text="POBREMA",
                  width=30,
                  font=('Arial', 20),
                  pady=3, padx=5,
                  command=lambda: ct4(4), variable=i, value=4)
bt4.place(x=150, y=430)

bt6 = Button(janela, text='SAIR', width=5,
             font=('Verdana', 12, 'bold'),
             bg='red', activebackground='#b30000', activeforeground='#f2f2f2',
             command=janela.quit)
bt6.place(x=720, y=550)


def qt2():

    lb1["text"] = "Questão 2"
    lb2["text"] = "Irei contatar meu         ."


bt1 = Radiobutton(janela, bg='#262626', fg='#b38f00', indicatoron=0, activebackground='#cccccc',
                  activeforeground='black', text="Advogado", width=30, font=('Arial', 20), pady=3, padx=5,
                  command=lambda: ct(1), variable=i, value=1)
bt1.place(x=150, y=250)

bt2 = Radiobutton(janela, bg='#262626', fg='#b38f00', indicatoron=0, text="Adivogado", width=30, font=('Arial', 20),
                  pady=3, padx=5, command=lambda: ct2(2), variable=i, value=2)
bt2.place(x=150, y=310)

bt3 = Radiobutton(janela, bg='#262626', fg='#b38f00',
                  indicatoron=0,
                  text="Adevogado", width=30, font=('Arial', 20), pady=3, padx=5, command=lambda: ct3(3), variable=i,
                  value=3)
bt3.place(x=150, y=370)

bt4 = Radiobutton(janela, bg='#262626', fg='#b38f00',
                  indicatoron=0,
                  text="Advogadu",
                  width=30,
                  font=('Arial', 20),
                  pady=3, padx=5,
                  command=lambda: ct4(4), variable=i, value=4)
bt4.place(x=150, y=430)

# COMENTÁRIOS


def q1erro():
    lb1 = Label(janela, text="Você tem algum PROBLEMA comigo?", font=("verdana", 25),
                bg='#262626', fg='white')
    lb1.place(x=90, y=110)


def q2erro():
    s = Label(text="A resposta da questão é\n\nADVOGADO", fg='white',
              font=('Arial', 20), padx=200, bg='black')
    s.place(x=50, y=420)


########################################


janela.mainloop()
