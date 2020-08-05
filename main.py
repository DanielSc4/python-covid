import init
import compute

def main():
	dataframes = init.importa()

	while (True):
		print("1) Casi in Italia;\n2) Casi in una regione;\n3) Casi in tutte le regioni.\n4) Exit")
		ino = input()
		if (ino == "1"):
			compute.draw_casi(dataframes, frequency = "d")
		elif (ino == "2"):
			regione = input("Inserisci la regione: ")
			compute.draw_by_region(dataframes, regione, frequency = "d")
		elif (ino == "3"):
			compute.draw_all_region(dataframes)
		elif (ino == "4"):
			exit()
		else:
			pass


if __name__ == "__main__":
	main()

