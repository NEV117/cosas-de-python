#Calcula factorial pro max 4k no fake 1 link mega
#Nicolas Escandon Varela 2205629
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

def principal():
    r = messagebox.askyesno(message="¿Quieres calcular un factorial?", title="uwu")
    while r == True:
        numero1 = simpledialog.askinteger("", "Digite un numero")
                
        total_factorial = calcularFactorial(numero1)
        

        reporteT.config(state="normal")
        reporteT.insert(INSERT, str(numero1) + "!" + " = " + total_factorial +"\n")
        reporteT.config(state="disable")

        r = messagebox.askyesno(message="¿Quieres calcular otro factorial?", title="uwu")

def calcularFactorial(numero1):
    if numero1 <0:
        numero1 = abs(numero1)
        x = 0
        total_factor = 1
        for x in range(1, numero1+1, 1):
            total_factor = total_factor * x

        return "-" + str(total_factor)
    else:
        x = 0
        total_factor = 1
        for x in range(1, numero1+1, 1):
            total_factor = total_factor * x

        return str(total_factor) 

def salir():
    raiz.destroy()

def borrar():
    reporteT.config(state="normal")
    reporteT.delete("1.0","end")
    reporteT.config(state="disable")

raiz = Tk()
raiz.geometry("450x260")
raiz.title("Programa que calcula factorial")


marco1 = Frame(raiz)
marco1.config(bd=3, relief="sunken")
marco1.pack(pady=10)
iniciarB = Button(marco1, text="Iniciar", command = principal)
iniciarB.grid(row=0,column=0,padx=3, pady=3)
salirB = Button(marco1, text="Salir", command=salir)
salirB.grid(row=0,column=1,padx=3, pady=3)
borrarB = Button(marco1, text="Borrar", command=borrar)
borrarB.grid(row=0,column=2,padx=3, pady=3)


marco2 = LabelFrame(raiz, text="Resultados")
marco2.config(bd=3, relief="sunken")
marco2.pack()
reporteT = Text(marco2)
reporteT.config(state="disable", width=50, height=10)
reporteT.grid(row=0, column=0)

raiz.mainloop()
