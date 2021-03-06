# Batteryboys
This is the repository for our assignment. We need to make solve a case by connecting houses to batteries in the most efficient ways. Multiple algorithms are used to establish the most efficient connections.
The Manhattan grid is used, and per grid the cable which connects the house to a battery have a cost of 9 (check config).
The houses all have a certain place in the map. This is given (check resources). The batteries begin with a given place, but later on we could move them. 
So, we pay for the batteries and the cable per grid, and our goal is to reduce the costs as much as possible.
To learn more about the case go to (http://heuristieken.nl/wiki/index.php?title=SmartGrid).

### Requirements
In requirements.txt you can find the packages used for this case. All code in this repository is written in Python 3.6
For Pandas we used pandas v0.23.4, and for matploblib we used version 3.0.2.
  
### Structure
In the map resources you can find all files we use. The map classes contains the House, Battery and map class we need for this assignment. In the map algorithms you can find all algorithms that were used for our case. The map results contains the results we found for the case. We plotted some algorithms so we could see how they would do, and if they really gave better results.  
  
### Testing
To run our code use:
python main.py.
You can choose which neighbourhood (1, 2 or 3) you want to use and which algorithm.
For our case it is better to use several algorithms, because sometimes the differential after a hillclimber gets a better result.
Therefore, you can choose the first algorithm, but after this the results of the algorithm are still given to the differential, which makes new generations and tries to get a cheaper neighbourhood. 
The first fits for map 3 do not work, because they only connect 149 houses to batteries while we only accept 150 connected houses as a valid outcome.
The test.py file in our repository is a unittester, which checks the code we upload. 

### State space
State space: The statespace is calculated (per neighbourhood) with the batteries and the houses. 
We have 5 batteries and 150 houses per neighbourhood, so the state space for one neighbourhood is:
5^150, which is 7.006492e+104. Each house will be connected to a battery, so per house there are 5 possibilities. 
This results in our calculation. 
So our equation is amount of batteries ^ amount of houses, therefore 5^150 per neighbourhood.

### Lower- and upperbounds:
These are the Lower- and upperbounds costs for our case, per neighbourhood.
The costs are for the grids only, so without the battery prices.
The bounds are for exercise A and B, where the batteries still have a specific spot.
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

### Comparison
We see that first_fit_houses gets slightly better results than the first_fit_batteries, but the results are not very good.
They do not really go below 46.000.
The differential evolution however, gets a result of around 31.000.
This means that the differential evolution gets a better score, and is therefore better for us to use.
The hillclimber at this moment gives around 32.000, which is better than the differential and much better than both the first_fits. It is best for us to first run the hillclimber, then the differential. This is faster than only running the differential (then we need more generations). Now, we first get fast and good results with the hillclimber, and these results we use as first generations for the differential. We see that most of the times, the differential evolution returns an even cheaper neighbourhood.

   
### Solutions for difficulties we found in our case
A big issue with the differential algorithm is that the function that calculates the scores places the houses in a shuffeled order. When not all houses were connected, the 'almost correct' answers would be discarded as wrong. Because of this, it is not non-deterministic. 
In the beginning, the hill climber needed a solution to begin with. So, if our first fit didn't connect the houses, the hillclimber would not work. We fixed this with the ability that our hillclimber connects houses to a battery, if there is enough power. It does not always needs to swap, it can also only connect one house. Another difficulty is that our hillclimber might find a local optimum, which could lead to a good, but not the best, solution. Therefore, we use the hillclimber and return these results to the differential algorithm, so it could calculate even more. Most of the time, our differential algorithm finds a better solution. 
###### Authors: Bram van den Heuvel, Wiebe Jelsma en Max Baneke.
