import customtkinter as ctk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Funciones de manejo de clientes
def view_client():
    selected_item = tree.selection()
    if selected_item:
        client_id = tree.item(selected_item, 'values')[0]
        messagebox.showinfo("Ver Cliente", f"Detalles del cliente con ID: {client_id}")

def add_client():
    messagebox.showinfo("Agregar Cliente", "Formulario para agregar cliente")

def edit_client():
    selected_item = tree.selection()
    if selected_item:
        client_id = tree.item(selected_item, 'values')[0]
        messagebox.showinfo("Editar Cliente", f"Formulario para editar cliente con ID: {client_id}")

def delete_client():
    selected_item = tree.selection()
    if selected_item:
        client_id = tree.item(selected_item, 'values')[0]
        #  eliminar el cliente de la base de datos
        tree.delete(selected_item)
        messagebox.showinfo("Eliminar Cliente", f"Cliente con ID: {client_id} eliminado")

def search_clients():
    search_term = search_var.get()
    #  consulta a la base de datos con el término de búsqueda

    # Para solo mostrar algo,  solo mostramos un mensaje
    messagebox.showinfo("Buscar Clientes", f"Buscar clientes con término: {search_term}")

# Inicialización de la ventana principal
app = ctk.CTk()
app.geometry("900x600")
app.title("Gestión de Clientes")
app.config(bg='#2b2b2b')

# Frame principal
main_frame = ctk.CTkFrame(app, fg_color='#2b2b2b')
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Título
title = ctk.CTkLabel(main_frame, text="Gestión de Clientes", font=('Arial', 24), fg_color='#2b2b2b', text_color='white')
title.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

# Campo de búsqueda
search_var = ctk.StringVar()
search_entry = ctk.CTkEntry(main_frame, textvariable=search_var, placeholder_text="Buscar cliente")
search_entry.grid(row=1, column=0, padx=20, pady=10, columnspan=3, sticky="ew")

search_button = ctk.CTkButton(main_frame, text="🔍", command=search_clients, fg_color='#3b3b3b', font=('Arial', 18))
search_button.grid(row=1, column=3, padx=20, pady=10)

# Tabla para mostrar los clientes
columns = ('ID', 'Nombre', 'Teléfono')  # se puede Ajustar las columnas según tu base de datos
tree = ttk.Treeview(main_frame, columns=columns, show='headings', style="Treeview")
tree.heading('ID', text='ID')
tree.heading('Nombre', text='Nombre')
tree.heading('Teléfono', text='Teléfono')
tree.grid(row=2, column=0, columnspan=4, padx=20, pady=10, sticky='nsew')

# Botones de funcionalidad
btn_view = ctk.CTkButton(main_frame, text="Ver Cliente", command=view_client, fg_color='#3b3b3b', font=('Arial', 18))
btn_view.grid(row=3, column=0, padx=20, pady=10)

btn_add = ctk.CTkButton(main_frame, text="Agregar Cliente", command=add_client, fg_color='#3b3b3b', font=('Arial', 18))
btn_add.grid(row=3, column=1, padx=20, pady=10)

btn_edit = ctk.CTkButton(main_frame, text="Editar Cliente", command=edit_client, fg_color='#3b3b3b', font=('Arial', 18))
btn_edit.grid(row=3, column=2, padx=20, pady=10)

btn_delete = ctk.CTkButton(main_frame, text="Eliminar Cliente", command=delete_client, fg_color='#3b3b3b', font=('Arial', 18))
btn_delete.grid(row=3, column=3, padx=20, pady=10)

# Configuracion el estiramiento de las columnas
main_frame.grid_rowconfigure(2, weight=1)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_columnconfigure(2, weight=1)
main_frame.grid_columnconfigure(3, weight=1)

# Ejecutar la aplicación
app.mainloop()
