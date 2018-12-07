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
![What is this](/results/First_fit_batteries_goede.png)

### First fit houses
1000 keer gerund, zien dat ie niet echt onder de 46000 komt.
![What is this](/results/first_fit_houses_goede.png)

#### Hill climber
hill climber tried 20.000 different swaps.
![What is this](/results/Hillclimber_try.png)

#### Genetic race

#### Differential evolution
Na een miljoen generaties waren de totale kosten voor map 1 63124.0. 
![What is this](/results/Differential_evolution_results.png)

#### Comparisson
We see that the firsT_fit_houses gets slightly better results than the first_fit_batteries, but the results are not very good.
They stop around 46.000.
The differential evolution however, gets a result of around 38.000.
This means that the differential evolution gets a better score, and is therefore better for us to use.
The hillclimber at this moment gives around 32.000, which is better than the differential and much better than both the first_fits.  

   
### Oplossingen voor pijnpunten in case

###### Auteurs (Authors): Bram van den Heuvel, Wiebe Jelsma en Max Baneke.
