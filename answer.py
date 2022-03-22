from tkinter import *;

#configuracion de la interfaz gráfica de usuario:
gui = Tk();
gui.title("Desarrollo parcial");
gui.geometry("280x240");

#valores:
boxSize = 30;

#Metodos:
def calcularValor():
    ubicacion = str(EUbicacion.get());
    tventa = str(ETipoVenta.get());
    cantidad = int(ECantidad.get());
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
    EValorVenta.delete(0, END);
    EValorVenta.insert(0, valtventa);
    EAporte.delete(0, END);
    EAporte.insert(0, aporte);
    

#creacion de elementos:
LUbicacion = Label(gui, text="Ubicacion");
EUbicacion = Entry(gui, width=boxSize);
LTipoVenta = Label(gui, text="Tipo de venta");
ETipoVenta = Entry(gui, width=boxSize);
LCantidad = Label(gui, text="Cantidad");
ECantidad = Entry(gui, width=boxSize)
BCalcularValor = Button(gui, command=calcularValor, text="Calcular valor");
LValorVenta = Label(gui, text="Valor venta");
EValorVenta = Entry(gui, width=boxSize);
LAporte = Label(gui, text="Valor aporte");
EAporte = Entry(gui, width=boxSize);

LUbicacion.pack();
EUbicacion.pack();
LTipoVenta.pack();
ETipoVenta.pack();
LCantidad.pack();
ECantidad.pack();
BCalcularValor.pack();
LValorVenta.pack();
EValorVenta.pack();
LAporte.pack();
EAporte.pack();

gui.mainloop();