from tkinter import *

#criar janela

root = Tk()
root.title("Login de Funcionario ")
fr1 = Frame(root)

#geometria
root.geometry('400x78+720+400')
root.resizable(width=False, height=False)

#criar os widgets

#---Frame 1---
lb0_fr1 = Label(fr1, text='Usuario:', font="Arial 20")
lb1_fr1 = Label(fr1, text='Senha:', font="Arial 20")

#--Frame 2 ---


#---Configuração do Frame---
fr1.grid()



#organizar os widgets

#---Frame 1---w
lb0_fr1.grid(row=0, column=2,sticky=W, padx=5)
lb1_fr1.grid(row=1, column=2,sticky=W, padx=5)

#---Frame 2---

#executar a janela
root.mainloop()
