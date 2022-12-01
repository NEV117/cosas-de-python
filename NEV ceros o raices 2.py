#Nicolas Escandon Varela 
#Version corregida en base a las pruebas del correo que se debian superar
from math import sqrt
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import *
from tkinter import simpledialog, messagebox
import cmath

simpledialog._QueryFloat.errormessage = 'El coeficiente debe ser un número real no fraccionario.'

def validar(self):
    try:
        result = self.getresult()
    except ValueError:
        messagebox.showwarning(
            "Coeficiente invalido",
            self.errormessage + "\nEjemplo: 1, -1, 1.2 \nEntre más decimales mayor exactitud ",
            parent = self
        )
        return 0

    if self.minvalue is not None and result < self.minvalue:
        messagebox.showwarning(
            "Muy pequeño",
            "El valor minimo permitido es %s. "
            "Intenta otra vez." % self.minvalue,
            parent = self
        )
        return 0

    if self.maxvalue is not None and result > self.maxvalue:
        messagebox.showwarning(
            "Muy largo",
            "El valor maximo permitido es %s. "
            "Intenta otra vez." % self.maxvalue,
            parent = self
        )
        return 0

    self.result = result

    return 1

simpledialog._QueryDialog.validate = validar

def principal():
    r = messagebox.askyesno(message="¿Quieres calcular los ceros o raíces de una ecuación cuadrática", title="")
    while r == True:
        A = simpledialog.askfloat("", "Coeficiente de Ax^2: ")
        B = simpledialog.askfloat("", "Coeficiente de Bx: ")
        C = simpledialog.askfloat("", "Coeficiente de C: ")

        ecua = '{0:+}'.format(A) + "X^(2) " + '{0:+}'.format(B) +"X " + '{0:+}'.format(C) + " = 0"
        x1 = 0
        x2 = 0

        if A == 0 and B == 0 and C == 0:
            respuesta = "\nInfinitas soluciones."
            
        elif A == 0 and B == 0:
            respuesta = "\nNo existe solución."
            
        elif A == 0:
            x1 = -C/B
            if x1 == -0.0:
                x1 = 0.0
            respuesta = "\nTiene una sola solución o raíz: " + "x = " + str(round(x1,3))

        elif ((B**2)-4*A*C) < 0:
            x1 = (-B+cmath.sqrt(B**2-(4*A*C)))/(2*A)
            x2 = (-B-cmath.sqrt(B**2-(4*A*C)))/(2*A)
            respuesta = "\nLas soluciones o raíces de la ecuación son:" + "\nx1 = " + str(complex(x1)).replace('j','i') + "\n" + "x2 = " + str(complex(x2)).replace('j','i')

        elif ((B**2)-4*A*C) == 0:
            x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
            x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
            respuesta = "\nTiene una sola solución o raíz: " + "x = " + str(round(x1,3))            
        
        else:
            x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
            x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
            respuesta = "\nLas soluciones o raíces de la ecuación son:\n" + "x1 = " + str(round(x1,3)) + "\n" + "x2 = " + str(round(x2,3))
            
        reporteT.config(state="normal")
        reporteT.insert(INSERT,"La ecuación introducida es:\n" + ecua + "\n" + respuesta + "\n\n" )
        reporteT.config(state="disable")

        r = messagebox.askyesno(message="Quieres calcular los ceros o raices de otra ecuación cuadrática?", title="")
            
def salir():
    raiz.destroy()

def borrar():
    reporteT.config(state="normal")
    reporteT.delete("1.0","end")
    reporteT.config(state="disable")

raiz = Tk()
raiz.geometry("450x260")
raiz.title("")

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
