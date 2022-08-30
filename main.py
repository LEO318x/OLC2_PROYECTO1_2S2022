import tkinter
from tkinter import Tk, Frame, Menu, messagebox, Text, Button, Label, filedialog

import Error.Errores
from aSintactico import analizar


class Ventana:
    def __init__(self, master=None):
        self.master = master
        self.master.title("OLC2_Proyecto1_2S2022")

        # Tamaño de nuestra ventana
        self.window_width = 1280
        self.window_height = 720

        # Obtenemos la dimención de la pantalla
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        # Buscamos el centro de la pantalla
        self.center_x = int(self.screen_width / 2 - self.window_width / 2)
        self.center_y = int(self.screen_height / 2 - self.window_height / 2)
        self.master.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')

        # Frame Analisis
        self.frmAnalisis = Frame(self.master)
        self.frmAnalisis.config(bg='#b6bab1')
        self.frmAnalisis.grid(row=0, column=0)
        self.frmAnalisis.rowconfigure(0, minsize=self.window_height, weight=1)

        self.txtEntrada = Text(self.frmAnalisis, width=72)
        self.txtEntrada.grid(row=0, column=1, padx=10, pady=5, sticky='NSWE')

        self.btnAbrir = Button(self.frmAnalisis, text='Abrir', width=10, command=self.fncAbrirArchivo)
        self.btnAbrir.grid(row=0, column=2, pady=20, sticky='N')

        self.btnAnalizar = Button(self.frmAnalisis, text='Analizar', width=10, command=self.fncAnalizar)
        self.btnAnalizar.grid(row=0, column=2, pady=80, sticky='N')

        self.txtSalida = Text(self.frmAnalisis, width=72)
        self.txtSalida.grid(row=0, column=3, padx=10, pady=5, sticky='NSWE')

        # Menú
        menu = Menu(self.master)
        self.master.config(menu=menu)

        editorMenu = Menu(menu, tearoff=0)
        editorMenu.add_command(label='Analisis', command=self.analisis_gui)
        menu.add_cascade(label='Editor', menu=editorMenu)

        reportesMenu = Menu(menu, tearoff=0)
        reportesMenu.add_command(label='Reporte de simbolos', command='')
        reportesMenu.add_command(label='Reporte de errores', command='')
        reportesMenu.add_command(label='Reporte de base de datos', command='')
        reportesMenu.add_command(label='Reporte de tablas de base de datos', command='')
        menu.add_cascade(label='Reportes.py', menu=reportesMenu)

        ayudaMenu = Menu(menu, tearoff=0)
        ayudaMenu.add_command(label='Acerca de', command=self.acerca_de)
        ayudaMenu.add_command(label='Salir', command=self.salir)
        menu.add_cascade(label='Ayuda', menu=ayudaMenu)

    def analisis_gui(self, master=None):
        self.frmAnalisis.grid()  # Mostramos el frame analisis

    def fncAbrirArchivo(self):
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )
        # Mostramos la ventana para seleccionar el archivo
        f = filedialog.askopenfile(filetypes=filetypes)
        if f:
            # Limpiamos nuestra area de texto correspondiente
            self.txtEntrada.delete(1.0, tkinter.END)
            # Leemos el archivo y ponemos el contenido en el area de texto correspondiente
            self.txtEntrada.insert('1.0', f.readlines())
        else:
            messagebox.showinfo(message="Por favor selecciona un archivo...", title="Información")

    def fncAnalizar(self):
        self.txtSalida.delete(1.0, tkinter.END)
        txt = self.txtEntrada.get('1.0', 'end-1c')
        analizar(txt)
        #print(f"Errores encontrrados{Error.Errores.lerrores}")
        # self.txtSalida.insert(tkinter.END, txt)

    @staticmethod
    def acerca_de():
        messagebox.showinfo(message="OLC2 PROYECTO 1 \n201212535 - Mike Leonel Molina García", title="Información")

    @staticmethod
    def salir() -> None:
        exit()


root = Tk()
miVentana = Ventana(root)
root.mainloop()
