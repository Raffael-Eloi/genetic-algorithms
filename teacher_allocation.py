import random

dataclasses = [[1, 27, 0], [2, 33, 0], [4, 25, 0], [4, 25, 1], [5, 42, 1], [1, 3, 0], [2, 26, 0], [3, 20, 0],
               [5, 45, 1], [6, 42, 1], [6, 20, 0], [5, 19, 0], [1, 43, 0], [6, 45, 0], [7, 30, 0], [2, 20, 0],
               [7, 30, 0], [3, 20, 0], [7, 27, 1], [2, 22, 0], [7, 26, 0], [4, 25, 0], [7, 25, 0], [4, 22, 0],
               [6, 30, 0], [1, 21, 0], [3, 25, 1], [3, 25, 0], [4, 44, 0], [5, 44, 1], [1, 25, 0], [3, 44, 0],
               [5, 44, 1]]

dataClassroom = [50, 20, 30, 40, 40, 50, 50, 40]


def createRChromosome(classroom: list, weekdays: list, classes: list) -> str:
    chromosome = classroom[random.randrange(0, len(classroom))][0]
    chromosome += weekdays[random.randrange(0, len(weekdays))]
    chromosome += classes[random.randrange(0, len(classes))][0]
    return chromosome


def createChromosome(classroom: list, weekdays: list, classes: list) -> str:
    chromosome = classroom[random.randrange(0, len(classroom))][0]
    chromosome += weekdays[random.randrange(0, len(weekdays))]
    chromosome += classes[0]
    return chromosome


def inicialization(classroom: list, weekdays: list, classes: list) -> list:
    listOfChromosomes = []
    for chromosome in range(67):
        chromosome = createRChromosome(classroom, weekdays, classes)
        listOfChromosomes.append(chromosome)
    for chromosome in classes:
        chromosome = createChromosome(classroom, weekdays, chromosome)
        listOfChromosomes.append(chromosome)
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
        classroom[i] = [classroom[i], dataClassroom[i]]
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
