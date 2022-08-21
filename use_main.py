from main import *

population = inicialization()

fitnessTeste = fitness(population)

print('All the population')
populationOrdered = bubbleSort(fitnessTeste)
show(populationOrdered) 

print('\n')
print('Best chromosome evaluation')

bestChromosome = getTheBestChromosome(fitnessTeste)
show([bestChromosome]) 

print('\n')
print('Top 10 Best chromosome')
bestChromosome = getTopTenChromosome(fitnessTeste)
show(bestChromosome) 