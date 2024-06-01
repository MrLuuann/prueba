
import tkinter as tk
from tkinter import ttk

# Funci�n para mostrar/ocultar la contrase�a
def toggle_password():
    if var.get():
        password_entry.config(show='')
    else:
        password_entry.config(show='*')

# Crear la ventana principal
root = tk.Tk()
root.title('Registro')
root.geometry('900x600')  # Ajusta el tama�o de la ventana aqu�
root.configure(bg='#D9D9D9')

# Frame para la secci�n de registro
left_frame = tk.Frame(root, bg='#D9D9D9')
left_frame.pack(side='left', fill='both', expand=True)

# Frame para la secci�n del logo y nombre del banco
right_frame = tk.Frame(root, bg='#3B9076')  # Cambia el color de fondo aqu�
right_frame.pack(side='right', fill='both', expand=True)



# Crear los campos de texto (textbox) en el frame izquierdo
labels = ['Nombre', 'Apellido paterno', 'Apelido materno', 'Fecha de nacimiento', 'CURP', 'Domicilio', 'Telefono', 'Correo electronico', 'Password']
entries = []
for i, label in enumerate(labels):
    tk.Label(left_frame, text=label, bg='#D9D9D9').grid(row=i, column=0, padx=10, pady=10, sticky='w')
    entry = ttk.Entry(left_frame)
    entry.grid(row=i, column=1, padx=5, pady=10)
    entries.append(entry)

# Configurar el campo de la contrase�a
password_entry = entries[-1]
password_entry.config(show='*')

# Checkbox para mostrar/ocultar la contrase�a
var = tk.IntVar()
checkbox = tk.Checkbutton(left_frame, text='Mostrar', variable=var, command=toggle_password, bg='#D9D9D9')
checkbox.grid(row=8, column=5, padx=10, pady=20)

# Bot�n para registrarse
register_button = tk.Button(left_frame, text='Registrarse', bg='#3B9076', fg='white')
register_button.grid(row=100, column=1, padx=20, pady=10)

# Aqu� puedes agregar el logo del banco y el nombre en el frame derecho
# Por ejemplo, puedes usar una etiqueta con una imagen y texto
bank_names = tk.Label(right_frame, text='BIENVENIDO!', bg='#3B9076', fg='white', font=('Harmmersmith One', 20))
bank_names.pack()
bank_logo = tk.PhotoImage(file='C:/Users/uriel/OneDrive/Documentos/practica vero python/Banco/IMAGENES/banco (1).png')  # Aseg�rate de tener el logo en el mismo directorio que tu script
logo_label = tk.Label(right_frame, image=bank_logo, bg='#3B9076')
logo_label.pack(pady=100)
bank_name = tk.Label(right_frame, text='Flux Bank', bg='#3B9076', fg='white', font=('Harmmersmith One', 25))
bank_name.pack()

root.mainloop()
