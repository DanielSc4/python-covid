# python-covid
Tool per la visualizzazione dei dati sul covid in Italia


I dati sono presi da ```https://github.com/pcm-dpc/COVID-19```

Con questo strumento è possibile visualizzare i grafici dei vari scenari:

###### Nuovi casi giornalieri in Italia:
![Alt text](./img/Figure_1.png?raw=true)

###### Nuovi casi giornalieri in una regione specifica:
![Alt text](./img/Figure_Lombardia.png?raw=true)

###### Nuovi casi giornalieri confrontando dati di diverse regioni:
![Alt text](./img/Figure_Lazio_Lomb_Pie_Venet.png?raw=true)

#### How does it work:

```init.py``` si occupa di effettuare la lettura dei files csv e di effettuare una prima pulizia dei dati

```compute.py``` si occupa di fare i calcoli necessari e di disegnare i grafici richiesti

Più nello specifico vengono utilizzate le librerie *pandas* per la gestione dei dataset, *numpy* per i calcoli e *matplotlib* per la rappresentazione grafica