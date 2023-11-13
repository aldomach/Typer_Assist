import tkinter as tk

def button_click(shortcut):
    text_field.insert(tk.END, shortcut)

root = tk.Tk()
root.title("Typertask GUI")
root.resizable(False, False)  # Impedir cambiar el tamaño de la ventana

# Crear botones para cada atajo
shortcuts = [
    "{Control}","{Alt}","{Shift}", "{tab}",
    "{left}", "{right}", "{down}", "{up}",
    "{enter}", "{return}",   "{insert}", 
    "{delete}", "{home}", "{pageup}",  "{pagedown}",
    "{backspace}", 
    "{controldown}", "{controlup}", "{shiftdown}", "{shiftup}",
    "{altdown}", "{altup}", "{delay=1000}", "{delay=500}","=RUN: ", 
    "{{yyyy}}", "{{yy}}", "{{mm}}", "{{dd}}", "{{hh}}", "{{uu}}",
     "{VolumeMute}", "{VolumeUp}","{VolumeDown}",
    "{Num1}", 
    "{Num2}", 
     "{F1}", "{F2}", "{F3}", "{F4}", "{F5}", "{F6}", "{F7}", "{F8}", "{F9}", "{F10}", "{F11}", "{F12}"
         
]

# Dividir los atajos en 4 columnas
columns = 8
rows = (len(shortcuts) + columns - 1) // columns

# Set the width of all buttons to 20
button_width = 12

for i in range(rows):
    for j in range(columns):
        index = i * columns + j
        if index < len(shortcuts):
            shortcut = shortcuts[index]
            button = tk.Button(root, text=shortcut, command=lambda s=shortcut: button_click(s), width=button_width)
            button.grid(row=i, column=j, padx=5, pady=5)

# Crear campo de texto para mostrar el atajo seleccionado
text_field = tk.Text(root, height=5, width=100)
text_field.grid(row=rows, columnspan=columns)

# Agregar margen de 15 píxeles en la parte superior e inferior de la ventana
root.wm_geometry("840x350+15+15")

root.mainloop()