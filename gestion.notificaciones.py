import customtkinter as ctk
from tkinter import messagebox

# Funciones de manejo de notificaciones
def view_notifications():
    messagebox.showinfo("Notificaciones", "Ver notificaciones de pólizas próximas a vencer")

def create_notification():
    messagebox.showinfo("Notificaciones", "Crear nueva notificación de vencimiento de póliza")

# Inicialización de la ventana principal
app = ctk.CTk()
app.geometry("800x600")
app.title("Notificaciones de Pólizas")
app.config(bg='#2b2b2b')

# Frame principal
main_frame = ctk.CTkFrame(app, fg_color='#2b2b2b')
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Título
title = ctk.CTkLabel(main_frame, text="Notificaciones de Pólizas", font=('Arial', 24), fg_color='#2b2b2b', text_color='white')
title.grid(row=0, column=0, columnspan=2, padx=20, pady=20)

# Botones de funcionalidad
btn_view = ctk.CTkButton(main_frame, text="Ver Notificaciones", command=view_notifications, fg_color='#3b3b3b', font=('Arial', 18))
btn_view.grid(row=1, column=0, padx=20, pady=10)

btn_create = ctk.CTkButton(main_frame, text="Crear Notificación", command=create_notification, fg_color='#3b3b3b', font=('Arial', 18))
btn_create.grid(row=1, column=1, padx=20, pady=10)

# Área de texto para visualizar notificaciones (para ilustración)
notifications_text = ctk.CTkTextbox(main_frame, width=400, height=200, fg_color='#4b4b4b', text_color='white')
notifications_text.grid(row=2, column=0, columnspan=2, padx=20, pady=20)
notifications_text.insert("0.0", "Aquí se mostrarán las notificaciones de vencimiento de pólizas...\n")

# Ejecutar la aplicación
app.mainloop()
