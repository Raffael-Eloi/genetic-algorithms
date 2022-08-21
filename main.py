import random
from transform import invertGene, tranformBinaryToFloat 

def createChromosome() -> str:
    chromosome = ''
    for gene in range(8):
        gene = random.randrange(0, 2)
        chromosome += str(gene)
    return chromosome

def inicialization() -> list:
    listOfChromosomes = []
    for chromosome in range(100):
        chromosome = createChromosome()
        listOfChromosomes.append( chromosome )
    return listOfChromosomes

def getFitnessValue(chromosome: str) -> list:
    fitnessList = [chromosome]
    fitnessList.append( tranformBinaryToFloat(chromosome) )
    return fitnessList

def fitness(listOfChromosomes: list) -> list:
    fitnessList = []
    for eachChromosome in listOfChromosomes:
        chromosomeWithValue = [eachChromosome]
        chromosomeWithValue.append( getFitnessValue(eachChromosome) )
        fitnessList.append(chromosomeWithValue)
    return fitnessList

def crossover(chromosome: str) -> str:
    newChromosome = ''
    for gene in chromosome:
        newChromosome += invertGene(gene)
    return newChromosome

def onePointCrossover(firstChromosome: str, secondChromosome: str) -> list:
    firstChromosomeModified = firstChromosome[:4] + secondChromosome[4:]
    secondChromosomeModified = secondChromosome[:4] + firstChromosome[4:]
    return [ firstChromosomeModified, secondChromosomeModified ]

def twoPointCrossover(firstChromosome: str, secondChromosome: str) -> list:
    firstChromosomeModified = firstChromosome[:2] + secondChromosome[2:6] + firstChromosome[6:]
    secondChromosomeModified = secondChromosome[:2] + firstChromosome[2:6] + secondChromosome[6:]
    return [ firstChromosomeModified, secondChromosomeModified ]

population = inicialization()
# print(fitness(population)) 



