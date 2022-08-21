from main import *

population = inicialization()

fitnessTeste = fitness(population)

# print('All the population')
# populationOrdered = bubbleSort(fitnessTeste)
# show(populationOrdered) 

# print('\n')
# print('Best chromosome evaluation')

# bestChromosome = getTheBestChromosome(fitnessTeste)
# show([bestChromosome]) 

# print('\n')
# print('Top 10 Best chromosome')
# bestChromosome = getTopTenChromosome(fitnessTeste)
# show(bestChromosome) 

# print('\n')
# print('Decimation selection')
# decimationSelectionPopulation = decimationSelection(fitnessTeste)
# show(decimationSelectionPopulation) 

# print('\n')
# print('Roulette selection')
# RouletteWhellSelectionPopulation = RouletteWhellSelection(fitnessTeste)
# show([RouletteWhellSelectionPopulation]) 

print('\n')
print('Tournament selection')
TournamentSelectionPopulation = TournamentSelection(fitnessTeste)
show([TournamentSelectionPopulation]) 