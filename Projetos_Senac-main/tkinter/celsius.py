from tkinter import *
#back-end
def calculo():
    if in0.get().replace('.','',1).isdigit():
        lb1['text']=(float(in0.get())*1.8)+32        

#front-end
root = Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
#widgets
lb0 = Label(root, text='Insira Cº', font='Arial 25')
in0 = Entry(root, font='Arial 25')
bt0 = Button(root, text='Obtenha F', font='Arial 25', command=calculo)
lb1 = Label(root, text='Resultado', font='Arial 25')

lb0.grid(row=0, column=0, sticky=NSEW)
in0.grid(row=0, column=1, sticky=NSEW)
bt0.grid(row=1, column=0, sticky=NSEW)
lb1.grid(row=1, column=1, sticky=NSEW)

root.mainloop()