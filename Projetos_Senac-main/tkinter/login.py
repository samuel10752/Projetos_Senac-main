from cgitb import text
from tkinter import*
from tkinter.ttk import Style

#janela 
root = Tk()
root.geometry('790x293+720+400') 


fr1 = LabelFrame(root, background='#ededed')
fr2 = LabelFrame(root, background='#ededed')
fr3 = Frame(root, background='#ededed')

#Dados Pessoais
Title_fr1 = Label (fr1, text='Dados Pessoais', font='Sans-Serif  20', fg='#993399')

#linha 1
Nome_fr1 = Label (fr1, text='Nome:', font="Sans-Serif  15", anchor=E)
Nomeinput_fr1 = Entry (fr1, font='Sans-Serif ')

#Linha 2
DataNasc_fr1 = Label (fr1, text='Data Nasc:', font="Sans-Serif  15")
Datainput_fr1 = Entry (fr1, font='Sans-Serif  ')

#Linha 3
CPF_fr1 = Label (fr1, text='CPF:', font="Sans-Serif  15")
CPFinput_fr1 = Entry (fr1, font='Sans-Serif  ')

#Linha 4
Telefone_fr1 = Label (fr1, text='Telefone:', font="Sans-Serif  15")
Telefoneinput_fr1 = Entry (fr1, font='Sans-Serif  ')


#Endereço

#Linha 5

Title2_fr2 = Label (fr2, text='Endereço', font='Sans-Serif  20', fg='#993399')

#linha 6
Rua_fr2 = Label (fr2, text='Rua:', font="Sans-Serif  15")
Ruainput_fr2 = Entry (fr2, font='Sans-Serif ')

#Linha 7
Bairro_fr2 = Label (fr2, text='Bairro:', font="Sans-Serif  15")
Bairroinput_fr2 = Entry (fr2, font='Sans-Serif ')


#Linha 8

Cidade_fr2 = Label (fr2, text='Cidade:', font="Sans-Serif  15")
Cidadeinput_fr2 = Entry (fr2, font='Sans-Serif ')

#Linha 9

N_fr2 = Label (fr2, text='N°:', font="Sans-Serif  15")
Ninput_fr2 = Entry (fr2, font='Sans-Serif ')

#Linha 10

UF_fr2 = Label (fr2, text='UF:', font="Sans-Serif  15")
UFinput_fr2 = Entry (fr2, font='Sans-Serif ')



############################Input#####################
Gravar_fr3 = Button(fr3, text='Gravar Dados', font='Sans-Serif  15')
imprimir_fr3 = Button(fr3,text='Imprimir dados', font='Sans-Serif  15')

#Frame
fr1.grid(sticky=W)
fr2.grid()
fr3.grid(sticky=W)


# Organizar os Widgets 

#Titulo 
Title_fr1.grid(row=0,  column=0, sticky=NSEW)

#Nome
Nome_fr1.grid(row=1, column=0,sticky=EW, padx=10)
Nomeinput_fr1.grid(row=1, column=1, sticky=EW, padx=10)

#Data Nasc
DataNasc_fr1.grid(row=2, column=0,  sticky=W, padx=10)
Datainput_fr1.grid(row=2, column=1,  sticky=W, padx=10)
#CPf
CPF_fr1.grid(row=3, column=0,  sticky=W, padx=10)
CPFinput_fr1.grid(row=3, column=1,  sticky=W, padx=10)

#Telefone
Telefone_fr1.grid(row=4, column=0,  sticky=W, padx=10)
Telefoneinput_fr1.grid(row=4,column=1,  sticky=W, padx=10)


#Endereço

#Titulo 
Title2_fr2.grid(row=0, column=0,sticky=NSEW)

#Rua
Rua_fr2.grid(row=1, column=0,sticky=NSEW)
Ruainput_fr2.grid(row=1, column=1,columnspan=3,sticky=NSEW)

#Bairro
Bairro_fr2.grid(row=2, column=0, sticky=NSEW)
Bairroinput_fr2.grid(row=2, column=1, sticky=NSEW)

#Cidade

Cidade_fr2.grid(row=2, column=2,sticky=NSEW)
Cidadeinput_fr2.grid(row=2, column=3,sticky=NSEW) 

#N°
N_fr2.grid(row=1, column=4, sticky=NSEW)
Ninput_fr2.grid(row=1, column=5, sticky=NSEW)

#UF
UF_fr2.grid(row=2, column=4, sticky=NSEW)
UFinput_fr2.grid(row=2, column=5, sticky=NSEW)

#Input
Gravar_fr3.grid(row=3, column=7, sticky=NSEW)
imprimir_fr3.grid(row=3, column=8,sticky=NSEW)

#Rodar
root.mainloop()