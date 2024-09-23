import customtkinter as ctk
from tkinter import messagebox

# Inicialización de la ventana principal
app = ctk.CTk() 
app.geometry("400x300")
app.title("Login - Gestoría de Seguros")
app.config(bg='#2b2b2b')

# Frame principal
login_frame = ctk.CTkFrame(app, fg_color='#2b2b2b')
login_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Título
title = ctk.CTkLabel(login_frame, text="Iniciar Sesión", font=('Arial', 24), fg_color='#2b2b2b', text_color='white')
title.pack(pady=20)

# Campo de entrada para el usuario
username_label = ctk.CTkLabel(login_frame, text="Usuario", font=('Arial', 16), fg_color='#2b2b2b', text_color='white')
username_label.pack(pady=(10, 0))
username_entry = ctk.CTkEntry(login_frame, placeholder_text="Ingrese su usuario", width=250)
username_entry.pack(pady=10)

# Campo de entrada para la contraseña
password_label = ctk.CTkLabel(login_frame, text="Contraseña", font=('Arial', 16), fg_color='#2b2b2b', text_color='white')
password_label.pack(pady=(10, 0))
password_entry = ctk.CTkEntry(login_frame, placeholder_text="Ingrese su contraseña", width=250, show="*")
password_entry.pack(pady=10)

# Función para manejar el inicio de sesión
def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # esto es para agregar la lógica para autenticar al usuario
    if username == "admin" and password == "password":
        messagebox.showinfo("Login", "Inicio de sesión exitoso")
        app.destroy()  # Cerrar la ventana de inicio de sesión después del login exitoso
        # aca es para abrir la ventana principal de la aplicación
    else:
        messagebox.showerror("Login", "Usuario o contraseña incorrectos")

# Botón de inicio de sesión
login_button = ctk.CTkButton(login_frame, text="Iniciar Sesión", command=login, font=('Arial', 16), fg_color='#3b3b3b')
login_button.pack(pady=20)

# Ejecutar la aplicación
app.mainloop()
