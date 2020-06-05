from tkinter import *

root = Tk()

ancho = 500
alto = 300

root.geometry(str(ancho)+"x"+str(alto))
root.resizable(0,0)
root.config(bg="silver")
root.title("Examen Final")

saludo = Label(text="Bienvenidos",font=("Times New Roman",20)).place(x=150,y=5)

lblname=Label(text="Nombre", font=("Arial",11)).place(x=70,y=30)
entrada=StringVar()
entrada.set("")
txtnombre=Entry(root,textvariable=entrada).place(x=135,y=40)

lblape=Label(text="Apellido", font=("Arial",11)).place(x=80,y=60)
entrada=StringVar()
entrada.set("")
txtape=Entry(root,textvariable=entrada).place(x=135,y=70)

lbldia=Label(text="Día",font=("Arial",11)).place(x=80,y=90)
entrada=StringVar()
entrada.set("")
txtdia=Entry(root,textvariable=entrada).place(x=135,y=100)

lblmes=Label(text="Mes",font=("Arial",11)).place(x=80,y=120)
entrada=StringVar()
entrada.set("")
txtmes=Entry(root,textvariable=entrada).place(x=135,y=130)

lblaño=Label(text="Año",font=("Arial",11)).place(x=80,y=150)
entrada=StringVar()
entrada.set("") 
txtaño=Entry(root,textvariable=entrada).place(x=135,y=160)


btnFuncion1 = Button(root, text= "Función  1",font=("Arial",10),width=10).place(x=20,y=190)
btnFuncion1 = Button(root, text= "Función 2",font=("Arial",10),width=10).place(x=115 ,y=190)
btnFuncion1 = Button(root, text= "Función 3",font=("Arial",10),width=10).place(x=211,y=190)
btnFuncion1 = Button(root, text= "Función 4",font=("Arial",10),width=10).place(x=305,y=190)
btnFuncion1 = Button(root, text= "Función 5",font=("Arial",10),width=10).place(x=400,y=190)









root.mainloop()
