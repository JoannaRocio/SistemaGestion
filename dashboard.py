import customtkinter as ctk
from tkinter import PhotoImage, ttk
import pandas as pd

# Inicialización de la ventana principal
app = ctk.CTk() 
app.geometry("1200x800")
app.title("Dashboard Gestoría de Seguros")
app.config(bg='#2b2b2b')

# Frame principal
main_frame = ctk.CTkFrame(app, fg_color='#2b2b2b')
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Panel lateral
sidebar = ctk.CTkFrame(main_frame, width=200, fg_color='#1e1e1e')
sidebar.grid(row=0, column=0, rowspan=2, sticky='ns', padx=(0, 10))

# Área de contenido
content_frame = ctk.CTkFrame(main_frame, fg_color='#2b2b2b')
content_frame.grid(row=0, column=1, sticky='nsew')

# Configuración de columnas y filas
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(0, weight=1)
content_frame.columnconfigure(0, weight=1)
content_frame.rowconfigure(0, weight=1)

# Título
title = ctk.CTkLabel(content_frame, text="Bienvenido a la Gestoría de Seguros", font=('Arial', 24), fg_color='#2b2b2b', text_color='white')
title.grid(row=0, column=0, padx=20, pady=20)

# Funcionalidad de los botones
def show_clients():
    update_content_frame("Clientes")
    
def manage_users():
    update_content_frame("Usuarios")

def generate_quotes():
    update_content_frame("Cotizaciones")

def notifications():
    update_content_frame("Notificaciones")

# Botones en el panel lateral
btn_clients = ctk.CTkButton(sidebar, text="Clientes", command=show_clients, fg_color='#3b3b3b', font=('Arial', 18))
btn_clients.pack(pady=10, padx=10, fill='x')

btn_users = ctk.CTkButton(sidebar, text="Usuarios", command=manage_users, fg_color='#3b3b3b', font=('Arial', 18))
btn_users.pack(pady=10, padx=10, fill='x')

btn_quotes = ctk.CTkButton(sidebar, text="Cotizaciones", command=generate_quotes, fg_color='#3b3b3b', font=('Arial', 18))
btn_quotes.pack(pady=10, padx=10, fill='x')

btn_notifications = ctk.CTkButton(sidebar, text="Notificaciones", command=notifications, fg_color='#3b3b3b', font=('Arial', 18))
btn_notifications.pack(pady=10, padx=10, fill='x')

# Actualización del área de contenido
def update_content_frame(text):
    for widget in content_frame.winfo_children():
        widget.destroy()  # Limpiar el área de contenido
        
    label = ctk.CTkLabel(content_frame, text=f"Vista de {text}", font=('Arial', 20), fg_color='#2b2b2b', text_color='white')
    label.grid(row=0, column=0, padx=20, pady=20)

    if text == "Clientes":
        # Ejemplo de tabla con pandas
        data = {
            'Nombre': ['Juan Pérez', 'Ana Gómez', 'Luis Fernández'],
            'Teléfono': ['123456789', '987654321', '456789123']
        }
        df = pd.DataFrame(data)

        table_frame = ctk.CTkFrame(content_frame, fg_color='#2b2b2b')
        table_frame.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

        tree = ttk.Treeview(table_frame, columns=list(df.columns), show='headings', style='Treeview')
        tree.pack(fill='both', expand=True)

        for col in df.columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        for index, row in df.iterrows():
            tree.insert('', 'end', values=list(row))

# Logo
logo = PhotoImage(file='images/logo.png')  # Actualiza la ruta del logo
logo_label = ctk.CTkLabel(content_frame, image=logo, text="")
logo_label.grid(row=2, column=0, pady=20)

# Ejecutar la aplicación
app.mainloop()
