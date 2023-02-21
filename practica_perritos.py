import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import pandas as pd

#Leemos el csv con la información
dogData = pd.read_csv('muestra_perros.csv')

#Inicialización de la interfaz.
root = tk.Tk()
root.title('Iterface')
root.geometry('600x350')

#Gráfica de la edad de los perros:
dogAgesFrame = pd.DataFrame(dogData)
dogAgesGraphic = plt.figure(figsize=(6, 3), dpi = 100)
ax1 = dogAgesGraphic.add_subplot(111)
bar1 = FigureCanvasTkAgg(dogAgesGraphic, root)
bar1.get_tk_widget().pack(side = tk.LEFT, fill = tk.NONE)
dogAgesFrame = dogAgesFrame[['edad']].round(decimals = 0).value_counts().sort_index()
dogAgesFrame.plot(kind='bar', legend=False, ax = ax1)
ax1.set_title('Distribución de perros por edad')


root.mainloop()