import init
import compute

def main():
	dataframes = init.importa()

	compute.draw_casi(dataframes, frequency = "d")
	compute.draw_by_region(dataframes, regione = "Lombardia", frequency = "d")
	compute.draw_all_region(dataframes)


if __name__ == "__main__":
	main()

