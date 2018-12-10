# Batteryboys
Dit is de repository voor het maken van een schema wat huizen zo efficiënt mogelijk koppelt aan een aantal batterijen.

### Vereisten
In requirements.txt staan de benodigde packages. Alle code in de repository is geschreven in Python 3.6.
  
### Structuur (Structure)
In de resources map staan alle bestanden die worden uitgelezen. De classes map bestaat uit de verschillende classes die zijn aangemaakt. De algorithms map bestaat uit alle algoritmes die gebruikt worden voor de case. Results heeft alle afbeeldingen van resultaten van het runnen van algoritmes.
  
### Test (Testing)
Om de code te draaien met de standaardconfiguratie gebruik de instructie:
python main.py.

### State space
State space: The statespace is calculated (per neighbourhood) with the batteries and the houses. 
We have 5 batteries and 150 houses per neighbourhood, so the state space for one neighbourhood is:
5^150, which is 7.006492e+104. Each house will be connected to a battery, so per house there are 5 possibilities. 
This results in our calculation. 
The state space will differ once we decide to add/remove batteries, because then the amount of batteries is different.
Then, we will use N^150, where N is the number of batteries.

#### Lower- and upperbounds:
These are the Lower- and upperbounds costs for our case, per neighbourhood.
The costs are for the grids only, so without the battery prices
Map 1:
lowerbound: 28188
upperbound: 78030
Map 2:
lowerbound: 20268
upperbound: 71253
Map 3:
lowerbound: 17757
upperbound: 76491
These are calculated with an algorithm, called bounds. Here we check the fursthest away and the closest battery to a house.

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

#### Comparison
We see that the firsT_fit_houses gets slightly better results than the first_fit_batteries, but the results are not very good.
They stop around 46.000.
The differential evolution however, gets a result of around 38.000.
This means that the differential evolution gets a better score, and is therefore better for us to use.
The hillclimber at this moment gives around 32.000, which is better than the differential and much better than both the first_fits.  

   
### Oplossingen voor pijnpunten in case
Een issue in het differentiaalevolutiealgoritme was dat de scorefunctie in een willekeurige volgorde de huizen zou verdelen over de batterijen. Dit zou niet uitmaken voor verdelingen waarin alle huizen passen, maar maakt wel degelijk uit als niet alle huizen passen. Echter bleek dit vooral een negatief effect te hebben, omdat bijna correcte antwoorden als foutief genoteerd konden worden. Om deze reden is de score niet niet-deterministisch.
Voor de hill climber was het essentieel om een eerste oplossing te krijgen om die vervolgens te optimaliseren. Een ander pijnpunt wat betreft de hill climber is het blijven steken van resultaten in lokale optima. Dit hebben we opgelost door de resultaatconfiguratie van huizen en batterij-verbindingen in een differentiaal algoritme te zetten.
###### Auteurs (Authors): Bram van den Heuvel, Wiebe Jelsma en Max Baneke.
