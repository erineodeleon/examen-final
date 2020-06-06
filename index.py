from tkinter import ttk
from tkinter import *
import math
import datetime
#ex, window
#fun1= es la funcion 1
#fun2= es la funcion 2
#fun3= es la funcion 3
#fun4= es la funcion 4
#fun5= es la funcion 5
#realizado por erineo :3
window = Tk()

class Desk:
    def __init__(ex, window):
        
        ex.wind = window
        
        ex.wind.geometry("700x400")
        ex.wind.resizable(0,0)
        ex.wind.config(bg="Gray")
        ex.wind.columnconfigure(1, weight=1)
        ex.wind.title("Examen Final")
        #BN TEXTO
        BN = LabelFrame(ex.wind, text = "Bienvenido",font=("Times New Roman",30))
        BN.grid(row = 0, column = 0, columnspan = 5, pady = 50)      
        Label(BN, text = "Nombre:",font=("arial",15)).grid(row = 1, column = 0)
        ex.fn1 = Entry(BN)
        ex.fn1.focus()
        ex.fn1.grid(row = 1, columnspan = 6)

        Label(BN, text = "Apellido: ",font=("arial",15)).grid(row = 2, column = 0)
        ex.fn2 = Entry(BN)
        ex.fn2.grid(row = 2, columnspan = 6)
        Label(BN, text = "Dia: ",font=("arial",15)).grid(row = 3, column = 0)
        ex.fn3 = Entry(BN)
        ex.fn3.grid(row = 3, columnspan = 6)

        Label(BN, text = "Mes: ",font=("arial",15)).grid(row = 4, column = 0)
        ex.fn4 = Entry(BN)
        ex.fn4.grid(row = 4, columnspan = 6)

        Label(BN, text = "Año: ",font=("arial",15)).grid(row = 5, column = 0)
        ex.fn5 = Entry(BN)
        ex.fn5.grid(row = 5, columnspan = 6)


        
        Button(BN, text = 'funcion1', command = ex.funcion1).grid(row = 6, column = 0 , sticky = W + E)
        Button(BN, text = 'funcion2', command = ex.funcion2).grid(row = 6, column = 1 , sticky = W + E)
        Button(BN, text = 'funcion3', command = ex.funcion3).grid(row = 6, column = 2 , sticky = W + E)
        Button(BN, text = 'funcion4', command = ex.funcion4).grid(row = 6, column = 3 , sticky = W + E)
        Button(BN, text = 'funcion5', command = ex.funcion5).grid(row = 6, column = 4 , sticky = W + E)
 



        ex.message = Label(text = '', fg = "green")
        ex.message.grid(row = 3, column = 0, columnspan = 2, sticky = W + E)

    
    def funcion1(ex):
        dia=int(ex.fn3.get())
        mes=int(ex.fn4.get())
        anio=int(ex.fn5.get())
        bindia=format(dia, '0b' )
        binmes=format(mes, '0b')
        binanio=format(anio, '0b')

        ex.message['text'] = 'La fecha es: {}/{}/{} y  en binario es:{}/{}/{}'.format(dia,mes,anio,bindia,binmes,binanio)


    def funcion2(ex):
            
        dia=int(ex.fn3.get())
        mes=int(ex.fn4.get())
        anio=int(ex.fn5.get())
        fecha_de_nacimiento = datetime.datetime(anio, mes, dia)
        fecha_de_hoy = datetime.datetime.now()
        diferencia = fecha_de_hoy - fecha_de_nacimiento
        dias_vividos = diferencia.days
        ex.message['text'] = 'Usted nacion {}/{}/{}: y a vivido {} dias'.format(dia,mes,anio,dias_vividos)

    def funcion3(ex):
        nombre=str(ex.fun1.get())
        apellido=str(ex.fn2.get())
        numero_nombre=int(len(nombre))
        numero_apellido=int(len(apellido))
        if numero_nombre%2==0 and numero_apellido %2==0 :
            ex.message['text'] = '{} {} su nombre es par y su apellido es par'.format(nombre,apellido)
        elif numero_nombre%2==0 and numero_apellido %2==1:
            ex.message['text'] = '{} {} su nombre es par y tu apellido es impar'.format(nombre,apellido)
        elif numero_nombre%2==1 and numero_apellido %2==0:
            ex.message['text'] = '{} {} su nombre es impar y tu apellido es par'.format(nombre,apellido)
        else:
            ex.message['text'] = '{} {} su nombre es impar y tu apellido es impar'.format(nombre,apellido)

    def funcion4(ex):
        nombre=str(ex.fn1.get())
        apellido=str(ex.fn2.get())
        cuenta = 0
        for carac in nombre:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
        for carac in apellido:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
        cuntal=len(nombre)
        cuntal1=len(apellido)
        consonante=cuntal+cuntal1-cuenta

        ex.message['text'] = 'Su nombre y apellido tienen {} vocales y {} consonantes'.format(cuenta,consonante)

    def funcion5(ex):
        nombre=str(ex.fn1.get())
        apellido=str(ex.fn2.get())
        cadena_invertida = ""
        cadena_invertida1= ""
        for letra in nombre:
            cadena_invertida = letra + cadena_invertida
        for letra1 in apellido:
            cadena_invertida1 = letra1 + cadena_invertida1
        ex.message['text'] = '{} {} o al revez {} {}'.format(nombre,apellido,cadena_invertida,cadena_invertida1)

if __name__ == '__main__':
    
    app = Desk(window)
    window.mainloop()
