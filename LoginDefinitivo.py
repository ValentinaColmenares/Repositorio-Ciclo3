import tkinter
from tkinter import *
from tkinter import messagebox

def inicio_sesion():
    global pantalla1
    pantalla1 = Tk()
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de Sesión")
    pantalla1.iconbitmap("login.ico")

    Label(pantalla1, text="Por favor ingrese su Usuario y Contraseña\n a continuación", bg="black", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(pantalla1, text="").pack()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry = Entry(pantalla1)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contrasena_usuario_entry = Entry(pantalla1, show="*")
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1,text="Iniciar Sesión", command=verificar).pack()

    pantalla1.mainloop()

def verificar():
    global count
    if nombre_usuario_entry.get() == "admin" and contrasena_usuario_entry.get() == "123":
        messagebox.showwarning('', 'Bienvenido, Inicio de sesión exitoso')
    else:
        if count != 1:
            messagebox.showwarning('', 'Datos incorrectos. Por favor, inténtelo otra vez.')
            count -= 1
        else:
            messagebox.showwarning('', 'Sistema bloqueado. Intente más tarde.')
            quit()

count = 3
inicio_sesion()