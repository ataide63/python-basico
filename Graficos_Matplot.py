


class graficos():
	global gerar
	import matplotlib.pyplot as gerar


	def Gerar_Grafico_Linhas():
		#   def Grafico_linha():
		from tkinter import Tk
		from tkinter import ttk
		from tkinter.messagebox import showinfo


		##     Can't find a usable init.tcl in the following directories:
		###    C:/Users/ataide/lib/tcl8.6 C:/Users/lib/tcl8.6 C:/lib/tcl8.6 C:/Users/library
		# #    C:/library C:/tcl8.6.12/library C:/tcl8.6.12/library



		# root = None
	

		x = [2,4,6,8]
		y = [7,5,9,1]
		gerar.title( "My first chart")
		gerar.plot(x,y)  # Linha
		gerar.show()
		


	def Gerar_Grafico_Barras():
		import numpy as np
		# Define the data

		N = 5
		menMeans = (20, 35, 30, 35, -27)
		womenMeans = (25, 32, 34, 20, -25)
		menStd = (2, 3, 4, 1, 2)
		womenStd = (3, 5, 2, 3, 3)
		ind = np.arange(N)    # the x locations for the groups
		width = 0.35       # the width of the bars: can also be len(x) sequence
		# Stacked bar plot with error bars

		fig, ax = gerar.subplots()

			# Define os valores das barras
		p1 = ax.bar(ind, menMeans, width, yerr=menStd, label='Men')
		p2 = ax.bar(ind, womenMeans, width,bottom=menMeans, yerr=womenStd, label='Women')

		ax.axhline(0, color='grey', linewidth=0.8)
		ax.set_ylabel('Scores')
		ax.set_title('Scores by group and gender')
		ax.set_xticks(ind, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
		ax.legend()

		# Label with label_type 'center' instead of the default 'edge'
		ax.bar_label(p1, label_type='center')
		ax.bar_label(p2, label_type='center')
		ax.bar_label(p2)

		gerar.show()
    

	def Gerar_Grafico_HorizBar(): 
		import numpy as np
		np.random.seed(19680801)

		## Example data
		people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
		y_pos = np.arange(len(people))
		performance = 3 + 10 * np.random.rand(len(people))
		error = np.random.rand(len(people))

		fig, ax = gerar.subplots()

		hbars = ax.barh(y_pos, performance, xerr=error, align='center')
		ax.set_yticks(y_pos, labels=people)
		ax.invert_yaxis()  # labels read top-to-bottom
		ax.set_xlabel('Performance')
		ax.set_title('How fast do you want to go today?')

		# Label with specially formatted floats
		ax.bar_label(hbars, fmt='%.2f')
		ax.set_xlim(right=15)  # adjust xlim to fit labels

		gerar.show()

	def Gerar_Graf_de_Dados():

		data = {'apple': 10, 'orange': 15, 'lemon': 5, 'lime': 20}
		names = list(data.keys())
		values = list(data.values())

		fig, axs = gerar.subplots(1, 3, figsize=(9, 3), sharey=True)
		axs[0].bar(names, values)
		axs[1].scatter(names, values)
		axs[2].plot(names, values)
		fig.suptitle('Categorical Plotting')
		gerar.show()


	def Gerar_Graficos_Eletro():

		import numpy as np

		fig, (ax1, ax2) = gerar.subplots(2, 1)
		# make a little extra space between the subplots
		fig.subplots_adjust(hspace=0.5)

		dt = 0.01
		t = np.arange(0, 30, dt)

		# Fixing random state for reproducibility
		np.random.seed(19680801)


		nse1 = np.random.randn(len(t))                 # white noise 1
		nse2 = np.random.randn(len(t))                 # white noise 2
		r = np.exp(-t / 0.05)

		cnse1 = np.convolve(nse1, r, mode='same') * dt   # colored noise 1
		cnse2 = np.convolve(nse2, r, mode='same') * dt   # colored noise 2

		# two signals with a coherent part and a random part
		s1 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse1
		s2 = 0.01 * np.sin(2 * np.pi * 10 * t) + cnse2

		ax1.plot(t, s1, t, s2)
		ax1.set_xlim(0, 5)
		ax1.set_xlabel('time')
		ax1.set_ylabel('s1 and s2')
		ax1.grid(True)

		cxy, f = ax2.csd(s1, s2, 256, 1. / dt)
		ax2.set_ylabel('CSD (db)')
		gerar.show()


###  Chamanado a classe  e o método dentro da classe
My_Class = graficos
# print(My_Class.Gerar_Grafico_Linhas())

# print(My_Class.Gerar_Grafico_Barras())

# print(My_Class.Gerar_Grafico_HorizBar())

#print(My_Class.Gerar_Graf_de_Dados())

print(My_Class.Gerar_Graficos_Eletro())

