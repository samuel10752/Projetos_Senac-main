from tkinter import *

#criar janela

root = Tk()
root.title("Login de Funcionario ")
fr1 = Frame(root)

#geometria
root.geometry('380x150+720+400')
#root.resizable(width=False, height=False)

#criar os widgets

#---Frame 1---
lb0_fr1 = Label(fr1, text='Usuario:', font="Arial 20")
lb1_fr1 = Label(fr1, text='Senha:', font="Arial 20")

#--Entrada ---
lb2_fr1 = Entry(fr1, font='Arial 18')
lb3_fr1 = Entry(fr1, font='Arial 18')
#--Button ---
tb0_fr1 = Button(fr1,text='Entrar', font="Arial 20",width=5)
tb1_fr1 = Button(fr1, text='Voltar', font="Arial 20",width=5)

#---Configuração do Frame---
fr1.grid()



#organizar os widgets

#---Frame 1---w
lb0_fr1.grid(row=0, column=2,sticky=W, padx=5)
lb1_fr1.grid(row=1, column=2,sticky=W, padx=5)

#--Entrada --
lb2_fr1.grid(row=0,column=2,sticky=W,padx=110)
lb3_fr1.grid(row=1,column=2,sticky=W,padx=110)

#---Butoon Função---
tb0_fr1.grid(row=3, column=2, sticky=W, padx=60)
tb1_fr1.grid(row=3, column=2, sticky=W,padx=180)
#executar a janel4
root.mainloop()