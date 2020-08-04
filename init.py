import pandas as pd
from os import listdir

def clean(dataframes):
	# drop delle righe con valori nulli (controlla dove la sigla della provincia è nulla)
	for i, df in enumerate(dataframes):
		dataframes[i] = df.dropna(subset = ["sigla_provincia"])
	return dataframes


def importa(path = "./data/"):
	# list of dataframes day by day
	dataframes = []
	files = listdir(path)

	# ordino i file secondo la data riportata nel nome
	files.sort()

	for file in files:
		if (file.endswith(".csv")):
			dataframes.append(pd.read_csv(path + file))
	# pulisco i dataframes
	dataframes = clean(dataframes)
	return dataframes



