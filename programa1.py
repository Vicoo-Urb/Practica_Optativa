from tkinter import *
import base64

#------------Propiedades de la venta----------
ventana=Tk()
ventana.title("Base 64")
ventana.resizable(0,0)
ventana.geometry("670x600")

#------------Definición de funciones-------------
def aceptar():
    global resultado1
    frase_texto = frase.get() 
    origen = frase_texto.encode("UTF-8")
    e = base64.b64encode(origen)
    resultado1 = e.decode("UTF-8")
    resultado.set(resultado1)

def decodificar():
    origen1 = resultado1.encode("UTF-8")
    d = base64.b64decode(origen1)
    frase2 = d.decode("UTF-8")
    frase_original.set(frase2)

#------------Propiedades de los textos principales-------------------
titulo = Label(ventana, text="Bienvenido", font=("Comic Sans MS", 25))
titulo.grid(row=1,column=1, columnspan=2, pady=10)

descripcion = Label(ventana, text="Este es un sistema capaz de cifrar y decifrar una frase en BASE64",  font=("Comic Sans MS", 15))
descripcion.grid(row=2,column=1, columnspan=2, pady=10)

instruccion = Label(ventana, text="Ingrese la frase a cifrar y luego presione aceptar", font=("Comic Sans MS", 13))
instruccion.grid(row=3,column=1, columnspan=2, pady=15)

#-------------Declaración de variables---------------------
frase = StringVar()
resultado = StringVar()
frase_original = StringVar()

#--------------Etiquetas y cuadros de textos-----------------
fraselab = Label(ventana, text="Frase", font=("Comic Sans MS", 12))
fraselab.grid(row=4, column=1,sticky="e")

ctxfrase = Entry(ventana,  font=("Comic Sans MS", 12), textvariable=frase )
ctxfrase.grid(row=4, column=2, ipadx=80, ipady=8, pady=15, sticky="w")

resultadolab = Label(ventana, text="Resultado", font=("Comic Sans MS", 13))
resultadolab.grid(row=5, column=1, pady=15, sticky="e")

ctxresultado = Entry(ventana, state='disabled', font=("Comic Sans MS", 12), textvariable=resultado)
ctxresultado.grid(row=5, column=2,  ipadx=80, ipady=8, pady=15, sticky="w")

#------------------Boton resultado-------------------------------
btaceptar = Button(ventana, text="Aceptar", font=("Comic Sans MS", 12), command=aceptar)
btaceptar.grid(row=6, column=1, columnspan=2)

#--------------Etiquetas y cuadros de textos-----------------
instruccion2 = Label(ventana, text="Para poder decifrar una frase es necesario primero haber cifrado una frase", font=("Comic Sans MS", 13))
instruccion2.grid(row=7,column=1, columnspan=2, pady=15)

result2lab = Label(ventana, text="Resultado", font=("Comic Sans MS", 13))
result2lab.grid(row=8, column=1, pady=15, sticky="e")

ctxresul2 = Entry(ventana,state='disabled',  font=("Comic Sans MS", 12),textvariable = frase_original)
ctxresul2.grid(row=8, column=2,  ipadx=80, ipady=8, pady=15, sticky="w")

#------------------Boton decodificar-------------------------------
btaceptar = Button(ventana, text="Decifrar", font=("Comic Sans MS", 12), command=decodificar)
btaceptar.grid(row=9, column=1, columnspan=2)

ventana.mainloop()