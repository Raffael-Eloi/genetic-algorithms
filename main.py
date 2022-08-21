import random
from transform import invertGeneValue, tranformBinaryToFloat, tranformBinaryToDecimal

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

def getFloatValue(chromosome: str) -> list:
    fitnessList = [chromosome]
    fitnessList.append( tranformBinaryToFloat(chromosome) )
    return fitnessList

def getFitnessValue(chromosomeNumber: float) -> float:
    return abs(2 - (chromosomeNumber * chromosomeNumber))

def fitness(listOfChromosomes: list) -> list:
    fitnessList = []
    for eachChromosome in listOfChromosomes:
        chromosomeWithValue = getFloatValue(eachChromosome)
        chromosomeWithValue[1] = getFitnessValue(chromosomeWithValue[1])
        chromosomeWithValue = getFloatValue(eachChromosome)
        fitnessList.append(chromosomeWithValue)
    return fitnessList

def bubbleSort(listOfChromosomes: list) -> list:
    quantityOfChromossomes = len(listOfChromosomes) - 1
    for eachQuantity in range(quantityOfChromossomes):
        for position in range(0, quantityOfChromossomes - eachQuantity):
            if listOfChromosomes[position][1] > listOfChromosomes[position + 1][1]:
                temporary = listOfChromosomes[position]
                listOfChromosomes[position] = listOfChromosomes[position + 1]
                listOfChromosomes[position + 1] = temporary
    return listOfChromosomes 

def crossover(chromosome: str) -> str:
    newChromosome = ''
    for gene in chromosome:
        newChromosome += invertGeneValue(gene)
    return newChromosome

def onePointCrossover(firstChromosome: str, secondChromosome: str) -> list:
    firstChromosomeModified = firstChromosome[:4] + secondChromosome[4:]
    secondChromosomeModified = secondChromosome[:4] + firstChromosome[4:]
    return [ firstChromosomeModified, secondChromosomeModified ]

def twoPointCrossover(firstChromosome: str, secondChromosome: str) -> list:
    firstChromosomeModified = firstChromosome[:2] + secondChromosome[2:6] + firstChromosome[6:]
    secondChromosomeModified = secondChromosome[:2] + firstChromosome[2:6] + secondChromosome[6:]
    return [ firstChromosomeModified, secondChromosomeModified ]

def show(listOfChromosome: list):
    for chromosome in listOfChromosome:
        print('Chromosome: {0} | Real number: {1} | Evaluation: {2}'.format(chromosome[0], tranformBinaryToDecimal(chromosome[0]), chromosome[1]) )

def sumAllFitnessValues(listOfChromosomes: list) -> float:
    totalFitnessValue = 0
    for eachChromosome in listOfChromosomes:
        totalFitnessValue += float(eachChromosome[1])
    return totalFitnessValue

def generateRandomNumber(inital: float, final: float) -> int:
    return random.uniform(inital, final+1)

def getTheBestChromosome(listOfChromosomes: list) -> list:
    listOfChromosomes = bubbleSort(listOfChromosomes)
    return listOfChromosomes[-1]

def getTopTenChromosome(listOfChromosomes: list) -> list:
    listOfChromosomes = bubbleSort(listOfChromosomes)
    initialPosition = int( len(listOfChromosomes) * 0.9 )
    return listOfChromosomes[initialPosition:]

def RouletteWhellSelection(listOfChromosomes: list) -> list: 
    totalFitnessValue = sumAllFitnessValues(listOfChromosomes)

def decimationSelection(listOfChromosomes: list) -> list:
    return getTopTenChromosome(listOfChromosomes)

# def TournamentSelection(listOfChromosomes: list) -> list: 
#     print('WIP - Working In Progress')



# print(generateRandomNumber(0,1))