import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def calcola_incremento(dataframes):
	# creo la lista di casi totali in italia day by day
	totali = []
	for i in range(0, len(dataframes)):
		# sommo i casi di oggi
		tot_oggi_sep = dataframes[i]["totale_casi"].tolist()
		oggi = sum(tot_oggi_sep)
		# sommo i casi di ieri
		if (i != 0):
			tot_ieri_sep = dataframes[i - 1]["totale_casi"].tolist()
			ieri = sum(tot_ieri_sep)
		else:
			ieri = oggi
		# i casi di oggi meno quelli di ieri da l'incremento giornaliero
		totali.append(oggi - ieri)
	return totali



def draw_casi(dataframes, frequency = "d"):
	# calcolo l'incremento giorno per giorno
	# frequency -> d = by day, w = by week (default day)
	if (frequency == "d"):
		totali = calcola_incremento(dataframes)
	elif (frequency == "w"):
		# TODO: ....
		print("ToDo")
	
	# ottenuti i casi totali disegno il grafo
	# x -> giorni
	# y -> numero casi
	plt.plot(range(0, len(dataframes)), totali, label='casi covid-19')  # Plot some data on the (implicit) axes.
	plt.xlabel('giorni')
	plt.ylabel('n casi')
	plt.title("Casi giornalieri coronavirus")
	plt.legend()

	plt.show()


