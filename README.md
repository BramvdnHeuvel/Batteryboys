# Batteryboys
Dit is de repository voor het maken van een schema wat huizen zo efficiënt mogelijk koppelt aan een aantal batterijen.

### Vereisten
In requirements.txt staan de benodigde packages. Alle code in de repository is geschreven in Python 3.6.
  
### Structuur (Structure)
In de resources map staan alle bestanden die worden uitgelezen. De classes map bestaat uit de verschillende classes die zijn aangemaakt. De algorithms map bestaat uit alle algoritmes die gebruikt worden voor de case. Results heeft alle afbeeldingen van resultaten van het runnen van algoritmes.
  
### Test (Testing)
Om de code te draaien met de standaardconfiguratie gebruik de instructie:
python main.py.

### Resultaten
Lower bound: De lower bound is berekend door elk huis aan de dichstbijzijnde batterij te koppelen.
Upper bound: De upper bound is berekend door elk huis aan de verste batterij te koppelen.
State space: De state space zou zijn dat elk huis in een hoek zou staan en gekoppeld wordt aan een batterij aan de andere kant van de kaart. Xmax = 50 en Ymax 50, Xmin = 0 en Ymin = 0. Om van een hoek naar de verste kant van de kaart te komen zullen dan 50*50 lijnen moeten worden getrokken wat 2500 lijnen geeft. Dit zou dan voor 150 huizen moeten gebeuren (met de aanname dat huizen onder elkaar mogen staan). Dit geeft een state space van 375000 lijnen om alle huizen aan een batterij te koppelen.


#### First fit batteries
1000 keer gerund, zien dat de resultaten boven de 46000 blijven.
![What is this](/results/first_fit/batteries.pdf)

### First fit houses
1000 keer gerund, zien dat ie niet echt onder de 46000 komt.
![What is this](/results/first_fit_houses.pdf)

#### Hill climber

#### Genetic race

#### Differential evolution
Na een miljoen generaties waren de totale kosten voor map 1 63124.0. 
![What is this](/results/Differential_evolution_results.png)

#### Smart-Grid
![What is this](/results/example grid.png)
   
### Oplossingen voor pijnpunten in case
Een issue in het differentiaalevolutiealgoritme was dat de scorefunctie in een willekeurige volgorde de huizen zou verdelen over de batterijen. Dit zou niet uitmaken voor verdelingen waarin alle huizen passen, maar maakt wel degelijk uit als niet alle huizen passen. Echter bleek dit vooral een negatief effect te hebben, omdat bijna correcte antwoorden als foutief genoteerd konden worden. Om deze reden is de score niet niet-deterministisch.

###### Auteurs (Authors): Bram van den Heuvel, Wiebe Jelsma en Max Baneke.
