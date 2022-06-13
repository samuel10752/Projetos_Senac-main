from tkinter import *
from tkinter.ttk import Labelframe

#criar janela

root = Tk()
fr1 = LabelFrame(root, bg='green')

#geometria
root.geometry('615x173+680+400')
root.overrideredirect(True)
root.resizable(width=False, height=False)

#criar os widgets

#---Frame 1---
lb0_fr1 = Label(fr1, text='Login do Funcionario', font='Arial 22',bg='green')
lb1_fr1 = Label(fr1, text='Usuario:', font="Arial 20",bg='green')
lb2_fr1 = Label(fr1, text='Senha:', font="Arial 20",bg='green')

#--Entrada ---
int0_fr1 = Entry(fr1, font='Arial 18', width=35)
int1_fr1 = Entry(fr1, font='Arial 18', width=35)
#--Button ---
tb0_fr1 = Button(fr1,text='Entrar', font="Arial 20",width=15,bg='black', fg='white')
tb1_fr1 = Button(fr1, text='Voltar', font="Arial 20",width=15,bg='black', fg='white')

#---Configuração do Frame---
fr1.grid()



#organizar os widgets

#---Frame 1---w
lb0_fr1.grid(row=0,column=1,sticky=W,padx=150)
lb1_fr1.grid(row=1, column=1,sticky=W, padx=5)
lb2_fr1.grid(row=2, column=1,sticky=W, padx=5)

#--Entrada --
int0_fr1.grid(row=1,column=1,sticky=W,padx=110)
int1_fr1.grid(row=2,column=1,sticky=W,padx=110)

#---Butoon Função---
tb0_fr1.grid(row=4, column=1, sticky=W, padx=55)
tb1_fr1.grid(row=4, column=1, sticky=E,padx=110)
#executar a janel4
root.mainloop()