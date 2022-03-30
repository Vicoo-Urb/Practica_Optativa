from tkinter import *

#Propiedades de la venta
ventana=Tk()
ventana.title("Base 64")
ventana.resizable(0,0)
ventana.geometry("670x700")


#Propiedades de los textos principales
titulo = Label(ventana, text="Bienvenido", font=("Comic Sans MS", 25))
titulo.grid(row=1,column=1, columnspan=2, pady=10)

descripcion = Label(ventana, text="Este es un sistema capaz de cifrar y decifrar una frase en BASE64",  font=("Comic Sans MS", 15))
descripcion.grid(row=2,column=1, columnspan=2, pady=10)

instruccion = Label(ventana, text="Ingrese la frase a cifrar y luego presione aceptar", font=("Comic Sans MS", 13))
instruccion.grid(row=3,column=1, columnspan=2, pady=15)

#Etiquetas y cuadros de textos
fraselab = Label(ventana, text="Frase", font=("Comic Sans MS", 12))
fraselab.grid(row=4, column=1,sticky="e")

ctxfrase = Entry(ventana,  font=("Comic Sans MS", 12))
ctxfrase.grid(row=4, column=2, ipadx=80, ipady=8, pady=15, sticky="w")

resultadolab = Label(ventana, text="Resultado", font=("Comic Sans MS", 13))
resultadolab.grid(row=5, column=1, pady=15, sticky="e")

ctxresultado = Text(ventana, state='disabled', font=("Comic Sans MS", 12), width=20, height=5)
ctxresultado.grid(row=5, column=2,  ipadx=80, ipady=8, pady=15, sticky="w")

#Boton resultado
btaceptar = Button(ventana, text="Aceptar", font=("Comic Sans MS", 12))
btaceptar.grid(row=6, column=1, columnspan=2)

instruccion2 = Label(ventana, text="Para poder decifrar una frase es necesario primero haber cifrado una frase", font=("Comic Sans MS", 13))
instruccion2.grid(row=7,column=1, columnspan=2, pady=15)

result2lab = Label(ventana, text="Resultado", font=("Comic Sans MS", 13))
result2lab.grid(row=8, column=1, pady=15, sticky="e")

ctxresul2 = Entry(ventana,state='disabled',  font=("Comic Sans MS", 12))
ctxresul2.grid(row=8, column=2,  ipadx=80, ipady=8, pady=15, sticky="w")

btaceptar = Button(ventana, text="Decifrar", font=("Comic Sans MS", 12))
btaceptar.grid(row=9, column=1, columnspan=2)

ventana.mainloop()