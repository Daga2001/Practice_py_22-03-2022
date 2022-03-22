datos = [[3, 7, 4],
[9, 6, 2],
[7, 5, 10]];

s = 0;

for i in range(0, 3, 1):
    for j in range(0, 3, 1):
        if(j==1):
            s = s + datos[i][j];
        else:
            s = s - datos[i][j];

#print(datos[2][2]);
#print(s);

#-----------------------------------------------------------------------------

references = [
    #["ubicacion", "tipo de venta", "precio boleto"],
    ["Palco", "Pre-venta", 22000],
    ["Palco", "Venta normal", 29000],
    ["Platea", "Pre-venta", 30000],
    ["Platea", "Venta normal", 38000],
];


from tkinter import *;
from functools import partial;

#configuracion de la interfaz gráfica de usuario:
gui = Tk();
gui.title("Desarrollo parcial");
gui.geometry("280x140");

#valores:
boxSize = 30;
valUbicacion = StringVar();
valTipoVenta = StringVar();
valCantidad = StringVar();
valValorVenta = StringVar();
valAporte = StringVar();

#Metodos:
def calcularValor(valUbicacion, valTipoVenta, valCantidad, valValorVenta, valAporte):
    ubicacion = (valUbicacion.get());
    tventa = (valTipoVenta.get());
    cantidad = int(valCantidad.get());
    valtventa = 0;
    if ubicacion == "Palco" and tventa == "Pre-venta":
        valtventa = 22000 * cantidad;
    elif ubicacion == "Palco" and tventa == "Venta normal":
        valtventa = 29000 * cantidad;
    elif ubicacion == "Platea" and tventa == "Pre-venta":
        valtventa = 30000 * cantidad;
    elif ubicacion == "Platea" and tventa == "Venta normal":
        valtventa = 38000 * cantidad;
    else:
        return "Valores invalidos, verifique nuevamente";
    aporte = valtventa * 0.15;
    valAporte.set(aporte);
    valValorVenta.set(valtventa);

#creacion de elementos:
LUbicacion = Label(gui, text="Ubicacion").grid(column=0, row=0);
EUbicacion = Entry(gui, textvariable=valUbicacion,width=boxSize).grid(column=1, row=0);
LTipoVenta = Label(gui, text="Tipo de venta").grid(column=0, row=1);
ETipoVenta = Entry(gui, textvariable=valTipoVenta,width=boxSize).grid(column=1, row=1);
LCantidad = Label(gui, text="Cantidad").grid(column=0, row=2);
ECantidad = Entry(gui, textvariable=valCantidad,width=boxSize).grid(column=1, row=2);
LValorVenta = Label(gui, text="Valor venta").grid(column=0, row=4);
EValorVenta = Entry(gui, textvariable=valValorVenta, width=boxSize).grid(column=1, row=4);
LAporte = Label(gui, text="Valor aporte").grid(column=0, row=5);
EAporte = Entry(gui, textvariable=valAporte, width=boxSize).grid(column=1, row=5);

calcularValor = partial(calcularValor, valUbicacion, valTipoVenta, valCantidad, valValorVenta, valAporte);
BCalcularValor = Button(gui, command=calcularValor, text="Calcular valor").grid(column=0, row=3);

gui.mainloop();


