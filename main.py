from tkinter import Tk, Menu, messagebox

class Ventana:
    def __init__(self, master=None):
        self.master = master
        self.master.title("OLC2_Proyecto1_2S2022")

        #Tamaño de nuestra ventana
        self.window_width = 1280
        self.window_height = 720

        # Obtenemos la dimención de la pantalla
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        # Buscamos el centro de la pantalla
        self.center_x = int(self.screen_width / 2 - self.window_width / 2)
        self.center_y = int(self.screen_height / 2 - self.window_height / 2)
        self.master.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')

        #Menú
        menu = Menu(self.master)
        self.master.config(menu=menu)

        ayudaMenu = Menu(menu, tearoff=0)
        ayudaMenu.add_command(label='Acerca de', command=self.acercade)
        ayudaMenu.add_command(label='Salir', command=self.salir)
        menu.add_cascade(label='Ayuda', menu=ayudaMenu)

    def acercade(self):
        messagebox.showinfo(message="OLC2 PROYECTO 1 \n201212535 - Mike Leonel Molina García", title="Información")

    def salir(self):
        exit()

root = Tk()
miVentana = Ventana(root)
root.mainloop()