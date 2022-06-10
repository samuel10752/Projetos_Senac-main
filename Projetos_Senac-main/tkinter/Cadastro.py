from cgitb import text
from tkinter import*
from tkinter.ttk import Style
from datetime import datetime
     

#Função / Data Nasc

def data(event=None):    
    x=Datainput_fr1.get().replace('/','')[:8]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [1,3]:
            y+=x[i] + '/'
        else:
            y+=x[i]
    Datainput_fr1.delete(0, 'end')
    Datainput_fr1.insert(0, y)
#CRÉDITO ao JeanExtreme002. Resposta disponível em: https://pt.stackoverflow.com/questions/492705/criando-um-entry-formatado-para-cpf-em-python-tkinter#:~:text=Para%20formatar%20o%20CPF%20enquanto,e%20a%20fun%C3%A7%C3%A3o%20de%20formata%C3%A7%C3%A3o.

#Verificador de CPF

def CPf(event=None):    
    x=CPFinput_fr1.get().replace('.','').replace('-', '')[:11]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '0123456789': continue
        if i in [2,5]:
            y+=x[i] + '.'
        elif i == 8:
            y+=x[i] + '-'
        else:
            y+=x[i]
    CPFinput_fr1.delete(0, 'end')
    CPFinput_fr1.insert(0, y)

#Vericficador de telefone

def telefone(event=None):    
    x=Telefoneinput_fr1.get().replace('(','').replace(')', '').replace('-','')[:11]
    y=''
    if event.keysym.lower() == "backspace": return
    for i in range(len(x)):
        if not x[i] in '00123456789': continue
        if i in []:
            y+=x[i] - '('
        if i in [1]:
            y+=x[i] + ')'   
        elif i == 6:
            y+=x[i] + '-'
        else:
            y+=x[i]
    Telefoneinput_fr1.delete(0, 'end')
    Telefoneinput_fr1.insert(0, y)

    

#janela 
root = Tk()
root.geometry('780x240+720+400') 
fr1 = LabelFrame(root, background='#ededed')
fr2 = LabelFrame(root, background='#ededed')
fr3 = Frame(root, background='#ededed')
#ededed
#Dados Pessoais
Title_fr1 = Label (fr1, text='Dados Pessoais', font='Sans-Serif  20')

#linha 1
Nome_fr1 = Label (fr1, text='Nome:', font="Sans-Serif  15")
Nomeinput_fr1 = Entry (fr1, font='Sans-Serif ', width=30)

#Linha 2
DataNasc_fr1 = Label (fr1, text='Data Nasc:', font="Sans-Serif  15")
Datainput_fr1 = Entry (fr1, font='Sans-Serif  ',width=9)
Datainput_fr1.bind("<KeyRelease>", data)

#Linha 3
CPF_fr1 = Label (fr1, text='CPF:', font="Sans-Serif  15")
CPFinput_fr1 = Entry (fr1, font='Sans-Serif  ', width=13)
CPFinput_fr1.bind("<KeyRelease>", CPf)

#Linha 4
Telefone_fr1 = Label (fr1, text='Telefone:', font="Sans-Serif  15")
Telefoneinput_fr1 = Entry (fr1, font='Sans-Serif  ',width=18)
Telefoneinput_fr1.bind("<KeyRelease>", telefone)


#Endereço

#Linha 5

Title2_fr2 = Label (fr2, text='Endereço', font='Sans-Serif  20')

#linha 6
Rua_fr2 = Label (fr2, text='Rua:', font="Sans-Serif  15")
Ruainput_fr2 = Entry (fr2, font='Sans-Serif ', width=25)

#Linha 7
Bairro_fr2 = Label (fr2, text='Bairro:', font="Sans-Serif  15")
Bairroinput_fr2 = Entry (fr2, font='Sans-Serif ', width=25)


#Linha 8

Cidade_fr2 = Label (fr2, text='Cidade:', font="Sans-Serif  15")
Cidadeinput_fr2 = Entry (fr2, font='Sans-Serif ')

#Linha 9

N_fr2 = Label (fr2, text='N°:', font="Sans-Serif  15")
Ninput_fr2 = Entry (fr2, font='Sans-Serif ', width=4)

#Linha 10

UF_fr2 = Label (fr2, text='UF:', font="Sans-Serif  15")
UFinput_fr2 = Entry (fr2, font='Sans-Serif ',width=3)



############################Input#####################
Gravar_fr3 = Button(fr3, text='Gravar Dados', font='Sans-Serif  15',bg='green')
imprimir_fr3 = Button(fr3,text='Imprimir dados', font='Sans-Serif  15',bg='green')

#Frame
fr1.grid()
fr2.grid()
fr3.grid()


# Organizar os Widgets 


#Titulo 
Title_fr1.grid(row=0,  column=1, sticky=EW, padx=0)

#Nome
Nome_fr1.grid(row=1, column=0,sticky=E)
Nomeinput_fr1.grid(row=1, column=1, sticky=E, padx=0)

#Data Nasc
DataNasc_fr1.grid(row=1, column=3, sticky=NSEW)
Datainput_fr1.grid(row=1, column=4, sticky=W)

#CPf
CPF_fr1.grid(row=3, column=0,  sticky=E)
CPFinput_fr1.grid(row=3, column=1,  sticky=W, padx=00)

#Telefone
Telefone_fr1.grid(row=3, column=3, sticky=W)
Telefoneinput_fr1.grid(row=3,column=4, sticky=W, padx=0)


#Endereço

#Titulo 
Title2_fr2.grid(row=0, column=1,sticky=E, padx=0)

#Rua
Rua_fr2.grid(row=1, column=0, sticky=E)
Ruainput_fr2.grid(row=1, column=1, sticky=E, padx=0)

#Bairro
Bairro_fr2.grid(row=2, column=0, sticky=E,padx=0)
Bairroinput_fr2.grid(row=2, column=1, sticky=E, padx=0)

#Cidade

Cidade_fr2.grid(row=1, column=2,sticky=W,padx=0)
Cidadeinput_fr2.grid(row=1, column=3,sticky=W, padx=0) 

#N°
N_fr2.grid(row=1, column=4, sticky=E)
Ninput_fr2.grid(row=1, column=5, sticky=W)

#UF
UF_fr2.grid(row=2, column=2, sticky=E)
UFinput_fr2.grid(row=2, column=3, sticky=W)

#Input
Gravar_fr3.grid(row=3, column=7, sticky=NSEW)
imprimir_fr3.grid(row=3, column=8,sticky=NSEW)

#Rodar
root.mainloop()