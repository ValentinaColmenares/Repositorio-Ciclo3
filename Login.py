import tkinter
from tkinter import *
from tkinter import messagebox

def menu_pantalla():
    global pantalla
    pantalla = Tk()
    pantalla.geometry("300x380")
    pantalla.title("Bienvenidos")
    pantalla.iconbitmap("login.ico")

    image = PhotoImage(file="welcome.gif")
    image = image.subsample(2,3)
    label = Label(image=image)
    label.pack()

    Label(text = "Acceso al sistema", bg="black", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(text="").pack()

    Button(text = "Iniciar sesión", height="3", width="30", command=inicio_sesion).pack()
    Label(text="").pack()

    Button(text = "Registar", height="3", width="30").pack()

    pantalla.mainloop()

def inicio_sesion():
    global pantalla1
    pantalla1 = Tk()
    #pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de Sesión")
    pantalla1.iconbitmap("login.ico")

    Label(pantalla1, text="Por favor ingrese su Usuario y Contraseña\n a continuación", bg="black", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(pantalla1, text="").pack()

    global nombreusuario_verify
    global contrasenausuario_verify

    nombreusuario_verify=StringVar()
    contrasenausuario_verify=StringVar()

    global nombre_usuario_entry
    global contrasena_usuario_entry

    Label(pantalla1, text="Usuario").pack()
    nombre_usuario_entry = Entry(pantalla1, textvariable=nombreusuario_verify)
    nombre_usuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contrasena_usuario_entry = Entry(pantalla1, show="*", textvariable=contrasenausuario_verify)
    contrasena_usuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1,text="Iniciar Sesión", command=verificar).pack()

    pantalla1.mainloop()

def verificar():
    print("Usuario: ", nombre_usuario_entry.get())
    print("Contraseña: ", contrasena_usuario_entry.get())
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