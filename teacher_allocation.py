import random
import time

dataclasses = [[1, 27, 0], [2, 33, 0], [4, 25, 0], [4, 25, 1], [5, 42, 1], [1, 3, 0], [2, 26, 0], [3, 20, 0],
               [5, 45, 1], [6, 42, 1], [6, 20, 0], [5, 19, 0], [1, 43, 0], [6, 45, 0], [7, 30, 0], [2, 20, 0],
               [7, 30, 0], [3, 20, 0], [7, 27, 1], [2, 22, 0], [7, 26, 0], [4, 25, 0], [7, 25, 0], [4, 22, 0],
               [6, 30, 0], [1, 21, 0], [3, 25, 1], [3, 25, 0], [4, 44, 0], [5, 44, 1], [1, 25, 0], [3, 44, 0],
               [5, 44, 1]]

dataClassroom = [[0, 50], [0, 20], [0, 30], [0, 40], [0, 40], [1, 50], [1, 50], [1, 40]]


def strToList(string: str) -> list:
    strLi = []
    strLi[:0] = string
    return strLi


def listToStr(listStr: list) -> str:
    return "".join(str(i) for i in listStr)


def twoPointCrossover(firstChromosome: list, secondChromosome: list):
    firstChromosomeModified = firstChromosome[0][:4] + secondChromosome[0][4:8] + firstChromosome[0][8:]
    secondChromosomeModified = secondChromosome[0][:4] + firstChromosome[0][4:8] + secondChromosome[0][8:]
    return [firstChromosomeModified, secondChromosomeModified]


def createChromosome(classroom: list, weekdays: list, classe: list) -> list:
    randClassroom = random.randrange(0, len(classroom))
    strChromosome = classroom[randClassroom][0]
    strChromosome += weekdays[random.randrange(0, len(weekdays))]
    strChromosome += classe[0]
    chromosome = [strChromosome, classroom[randClassroom][1], classroom[randClassroom][2], classe[1][0], classe[1][1],
                  classe[1][2]]
    return chromosome


def inicialization(classroom: list, weekdays: list, classes: list) -> list:
    listOfChromosomes = []
    for classe in classes:
        classe = createChromosome(classroom, weekdays, classe)
        listOfChromosomes.append(classe)
    return listOfChromosomes


def generateClassroomNumber(classroom: list) -> str:
    classroomCode = ''
    for i in range(4):
        classroomCode += str(random.randrange(0, 2))

    if classroomCode not in classroom:
        pass
    else:
        generateClassroomNumber(classroom)
    return classroomCode


def generateClassroom(quantityOfclassroom: int) -> list:
    classroom = []
    for i in range(quantityOfclassroom):
        classroom.append(generateClassroomNumber(classroom))
    for i in range(len(classroom)):
        classroom[i] = [classroom[i], dataClassroom[i][0], dataClassroom[i][1]]
    return classroom


def generateWeekdayNumber(weekdays: list) -> str:
    weekdayCode = ''
    for i in range(3):
        weekdayCode += str(random.randrange(0, 2))

    if weekdayCode not in weekdays:
        pass
    else:
        generateWeekdayNumber(weekdays)
    return weekdayCode


def generateWeekdays(quantityOfWeekdays: int) -> list:
    weekdays = []
    for i in range(quantityOfWeekdays):
        weekdays.append(generateWeekdayNumber(weekdays))
    return weekdays


def generateClassNumber(classes: list) -> str:
    classCode = ''
    for i in range(8):
        classCode += str(random.randrange(0, 2))

    if classCode not in classes:
        pass
    else:
        generateClassNumber(classes)
    return classCode


def generateClasses(quantityOfClasses: int) -> list:
    classes = []
    for i in range(quantityOfClasses):
        classes.append(generateClassNumber(classes))
    for i in range(len(classes)):
        classes[i] = [classes[i], dataclasses[i]]
    return classes


def TeacherPerDay(chromosome: list, population: list) -> float:
    for nChromosome in population:
        if chromosome[3] == nChromosome[3] and chromosome[0][4:7] == nChromosome[0][4:7] \
                and nChromosome[0] != chromosome[0]:
            return 0.5
    return 0


def ClassPerDay(chromosome: list, population: list) -> float:
    for nChromosome in population:
        if chromosome[0][:3] == nChromosome[0][:3] and chromosome[0][4:7] == nChromosome[0][4:7] \
                and nChromosome[0] != chromosome[0]:
            return 0.5
    return 0


def ClassPerClassroom(chromosome: list) -> float:
    if chromosome[2] <= chromosome[4]:
        return 0.5
    return 0


def corretLocation(chromosome: list) -> float:
    if chromosome[1] != chromosome[5]:
        return 0.5
    return 0


def fitness(population: list):
    nFitness = 0
    for chromosome in population:
        nFitness += TeacherPerDay(chromosome, population)
        nFitness += ClassPerDay(chromosome, population)
        nFitness += ClassPerClassroom(chromosome)
        nFitness += corretLocation(chromosome)
        chromosome.append(nFitness)
        nFitness = 0


def selection(population: list) -> list:
    population = sorted(population, key=lambda x: x[6])
    return population[:11]


def excludedSelection(population: list) -> list:
    population = sorted(population, key=lambda x: x[6])
    return population[11:]


def crossover(population: list) -> list:
    listPopulation = []
    population[0].pop()
    crossPopulation = population[1:]
    newPopulation = [(population[0])]
    for i in range(len(crossPopulation)):
        if (i % 2) == 0:
            crossChromosomes = twoPointCrossover(crossPopulation[i], crossPopulation[i + 1])
            listPopulation.extend(
                [crossChromosomes[0], crossPopulation[i][1], crossPopulation[i][2], crossPopulation[i][3],
                 crossPopulation[i][4], crossPopulation[i][5]])
            newPopulation.append(listPopulation)
            listPopulation = []
            listPopulation.extend(
                [crossChromosomes[1], crossPopulation[i + 1][1], crossPopulation[i + 1][2], crossPopulation[i + 1][3],
                 crossPopulation[i + 1][4], crossPopulation[i + 1][5]])
            newPopulation.append(listPopulation)
            listPopulation = []
    return newPopulation


def mutation(population: list) -> list:
    chromossomeMutation = random.randrange(0, len(population))
    geneMutation = random.randrange(0, len(population[chromossomeMutation][0]))
    listStr = strToList(population[chromossomeMutation][0])
    if listStr[geneMutation] == "1":
        listStr[geneMutation] = "0"
    else:
        listStr[geneMutation] = "1"
    population[chromossomeMutation][0] = listToStr(listStr)


def update(newPopulation: list, excludedPopulation: list, classroom: list, weekdays: list) -> list:
    classes = []
    for excludedChromossome in excludedPopulation:
        classes.append([excludedChromossome[0][7:], [excludedChromossome[3], excludedChromossome[4], excludedChromossome[5]]])
    population = inicialization(classroom, weekdays, classes)
    for chromossome in newPopulation:
        population.append(chromossome)
    return population


def zeroVerify(population: list) -> bool:
    count = 0
    for chromosome in population:
        if chromosome[6] == 0:
            count += 1
    if count >= 13:
        return True
    return False


def finishing(population: list, gen: int) -> bool:
    if zeroVerify(population):
        print("Finalizado por ter 13 ou mais avaliações máximas")
        print("Se passaram", gen, "gerações")
        print(sorted(population, key=lambda x: x[6]))
        return True
    if gen == 100000:
        print("Finalizado por ter se passado 100.000 gerações")
        print("Se passaram", gen, "gerações")
        print(sorted(population, key=lambda x: x[6]))
        return True
    return False
