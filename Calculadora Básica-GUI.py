#Ejercicio Calculardora Básica
#Nicolas Escandon Varela 2205629
#UWU
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from math import pi
import math

def principal():
    r = simpledialog.askinteger("Calculadora\tBásica", " 1. Sumar dos números.\n 2. Restas dos números\n 3. Multiplicar\n 4. Division entera\n 5. Residuo\n 6. Potencia\n 7. Factorial\n 8. Cambio de base\n 9. Tangente\n 10. Fin\n Digite la opción : ")

    while r != 10:
        if r ==1:
            numero1 = simpledialog.askinteger("", "Digite un numero")
            numero2 = simpledialog.askinteger("", "Digite un numero")

            total_suma = calcularSuma(numero1, numero2)

            reporteT.config(state="normal")
            reporteT.insert(INSERT, str(numero1)+ " + " + str(numero2)+ " = " + str(total_suma)+"\n")
            reporteT.config(state="disable")
            
        elif r == 2:
            numero1 = simpledialog.askinteger("", "Digite un numero")
            numero2 = simpledialog.askinteger("", "Digite un numero")

            total_resta = calcularResta(numero1, numero2)

            reporteT.config(state="normal")
            reporteT.insert(INSERT,str(numero1) + " - " + str(numero2) + " = " + str(total_resta)+"\n")
            reporteT.config(state="disable")
            
        elif r == 3:
            numero1 = simpledialog.askinteger("", "Digite un numero")
            numero2 = simpledialog.askinteger("", "Digite un numero")

            total_multiplicacion = calcularMultiplicacion(numero1, numero2)

            reporteT.config(state="normal")
            reporteT.insert(INSERT,str(numero1)+ " * " + str(numero2) + " = " + str(total_multiplicacion)+"\n")
            reporteT.config(state="disable")
            
        elif r == 4:
            numero1 = simpledialog.askinteger("", "Digite un numero")
            numero2 = simpledialog.askinteger("", "Digite un numero")

            total_division = calcularDivision(numero1, numero2)

            reporteT.config(state="normal")
            reporteT.insert(INSERT,str(numero1) + " // " + str(numero2) + " = " + str(total_division)+"\n")
            reporteT.config(state="disable")

        elif r == 5:
            numero1 = simpledialog.askinteger("", "Digite un numero")
            while numero1 < 0:
                messagebox.showerror(message="Eror, debe ingresar un valor positivo", title="")
                numero1 = simpledialog.askinteger("", "Digite un numero")
            numero2 = simpledialog.askinteger("", "Digite un numero")

            while numero2 < 0:
                messagebox.showerror(message="Eror, debe ingresar un valor positivo", title="")

                numero1 = simpledialog.askinteger("", "Digite un numero")

            total_residuo = calcularResiduo(numero1, numero2)

            reporteT.config(state="normal")
            reporteT.insert(INSERT, str(numero1) + " % " + str(numero2) + " = " + str(total_residuo)+"\n")
            reporteT.config(state="disable")

        elif r == 6:
            numero1 = simpledialog.askinteger("", "Digite un numero")
            numero2 = simpledialog.askinteger("", "Digite un numero")

            total_potencia = calcularPotencia(numero1, numero2)

            reporteT.config(state="normal")
            reporteT.insert(INSERT, str(numero1)+ " ** " + str(numero2) + " = " + str(total_potencia)+"\n")
            reporteT.config(state="disable")

        elif r == 7:
            numero1 = simpledialog.askinteger("", "Digite un numero")
            while numero1 <0:
                messagebox.showerror(message="Eror, debe ingresar un valor positivo", title="")
                numero1 = simpledialog.askinteger("", "Digite un numero")

            total_factorial = calcularFactorial(numero1)

            reporteT.config(state="normal")
            reporteT.insert(INSERT, str(numero1) + "!" + " = " + str(total_factorial)+"\n")
            reporteT.config(state="disable")

        elif r == 8:
            numero1 = simpledialog.askinteger("", "Digite un numero")
            numero2 = simpledialog.askinteger("", "Digite un numero")

            total_cambio = cambioBase(numero1, numero2)

            reporteT.config(state="normal")
            reporteT.insert(INSERT, "El número " + str(numero1) + " en base " + str(numero2) + " es: " + str(total_cambio)+"\n")
            reporteT.config(state="disable")

        elif r == 9:
            numero1 = simpledialog.askinteger("", "Digite un numero")

            total_tangente = calcularTangente(numero1)

            reporteT.config(state="normal")
            reporteT.insert(INSERT, "Tangente(" + str(numero1) + "°) es: " + str(total_tangente)+"\n")
            reporteT.config(state="disable")

        else:
            messagebox.showerror(message="Error debe ingresar un número entre 1 y 10", title ="")

        r = simpledialog.askinteger("Calculadora\tBásica", " 1. Sumar dos números.\n 2. Restas dos números\n 3. Multiplicar\n 4. Division entera\n 5. Residuo\n 6. Potencia\n 7. Factorial\n 8. Cambio de base\n 9. Tangente\n 10. Fin\n Digite la opción : ")


def calcularSuma(numero1, numero2):
    total_suma = numero1 + numero2

    return total_suma

def calcularResta(numero1, numero2):
    total_resta = numero1 - numero2

    return total_resta

def calcularMultiplicacion(numero1, numero2):
    if numero1 == 0 or numero2 == 0:
        total_multiplicacion = 0
    else:
        total_multiplicacion = 0
        x = 0
        if numero2 < 0:
            for x in range (0, numero2, -1):
                total_multiplicacion = total_multiplicacion - numero1
                
        else:
            for x in range (0, numero2, 1):
                total_multiplicacion = total_multiplicacion + numero1

        return total_multiplicacion
    
def calcularDivision(numero1, numero2):
    if numero2 == 0:
        total_division = "No se puede dividir entre 0"
    elif numero1 == 0:
        total_division = 0
    else:
        x = 0
        n1 = abs(numero1)
        n2 = abs(numero2)
        while n1 >= n2:
            n1 = n1 - n2
            x = x + 1
        total_division = x

        if (numero1<0)^(numero2<0):
            if x != 0:
                total_division = - x

    return total_division

def calcularResiduo(numero1, numero2):
    while numero1 >= numero2:
        numero1 = numero1 - numero2

    total_residuo = numero1

    return total_residuo

def calcularPotencia(numero1, numero2):
    if numero1 == 0:
        total_potencia = 1
        
    else:
        total_potencia = 1
        x = 0
        if numero2 < 0:
            for x in range (0, numero2, -1):
                total_potencia = total_potencia * numero1
                
            total_potencia = 1 / total_potencia

        else:
            for x in range (0, numero2, 1):
                total_potencia = total_potencia * numero1
                
    return total_potencia

def calcularFactorial(numero1):
    x = 0
    total_factor = 1
    for x in range(1, numero1+1, 1):
        total_factor = total_factor * x

    return total_factor

def cambioBase(numero1, numero2):
    resultado = ""
    while numero1 >= numero2:
        resultado = str(numero1%numero2) + resultado
        numero1 = numero1 // numero2
    resultado = str(numero1) + resultado

    return resultado
    
def calcularTangente(numero1):
    angulo = numero1 * pi/180

    tangente = math.tan(angulo)

    return round(tangente,4)
        
   
#Función Salir del aplicativo
def salir():
    raiz.destroy()

def borrar():
    reporteT.config(state="normal")
    reporteT.delete("1.0","end")
    reporteT.config(state="disable")

    
#Interfaz Gráfica de usuario
raiz = Tk()
raiz.geometry("450x260")
raiz.title("Calculadora Básica")

#contenedor Botones
marco1 = Frame(raiz)
marco1.config(bd=3, relief="sunken")
marco1.pack(pady=10)
iniciarB = Button(marco1, text="Iniciar", command = principal)
iniciarB.grid(row=0,column=0,padx=3, pady=3)
salirB = Button(marco1, text="Salir", command=salir)
salirB.grid(row=0,column=1,padx=3, pady=3)
borrarB = Button(marco1, text="Borrar", command=borrar)
borrarB.grid(row=0,column=2,padx=3, pady=3)


#contenedor Resultado
marco2 = LabelFrame(raiz, text="Resultados")
marco2.config(bd=3, relief="sunken")
marco2.pack()
reporteT = Text(marco2)
reporteT.config(state="disable", width=50, height=10)
reporteT.grid(row=0, column=0)


raiz.mainloop()
