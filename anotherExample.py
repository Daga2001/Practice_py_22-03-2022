from tkinter import *;

def calculator():
    a=int(EValorA.get());
    potencia=a*a;
    EResultado.delete(0,END);
    EResultado.insert(0,potencia);

gui = Tk();
gui.geometry("140x130");

LValorA =Label(gui,text="Valor a");
LResultado = Label(gui, text ="Resultado");
EValorA = Entry(gui, width=10);
EResultado = Entry(gui, width=20);
BPotencia = Button(gui, text="Calcular a 2", command=calculator)

LValorA.pack();
EValorA.pack();
BPotencia.pack();
LResultado.pack();
EResultado.pack();

gui.mainloop();