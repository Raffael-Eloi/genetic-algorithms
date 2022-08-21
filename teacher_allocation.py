import random

def createChromosome(classroom: list, weekdays: list, classes: list) -> str:
    chromosome = ''
    chromosome += classroom[ random.randrange(0, len(classroom)) ]
    chromosome += weekdays[ random.randrange(0, len(weekdays)) ]
    chromosome += classes[ random.randrange(0, len(classes)) ]
    return chromosome


def inicialization(classroom: list, weekdays: list, classes: list) -> list:
    listOfChromosomes = []
    for chromosome in range(100):
        chromosome = createChromosome(classroom, weekdays, classes)
        listOfChromosomes.append(chromosome)
    return listOfChromosomes

def generateClassroomNumber(classroom: list) -> str:
    classroomCode = ''
    for i in range (4):
        classroomCode += str( random.randrange(0, 2) )
    
    if classroomCode in classroom: generateClassroomNumber(classroom) 
    return classroomCode

def generateClassroom(quantityOfclassroom: int) -> list:
    classroom = []
    for i in range(quantityOfclassroom):
        classroom.append( generateClassroomNumber(classroom) )
    return classroom

def generateWeekdayNumber(weekdays: list) -> str:
    weekdayCode = ''
    for i in range (3):
        weekdayCode += str( random.randrange(0, 2) )
    
    if weekdayCode in weekdays: generateWeekdayNumber(weekdays) 
    return weekdayCode

def generateWeekdays(quantityOfWeekdays: int) -> list:
    weekdays = []
    for i in range(quantityOfWeekdays):
        weekdays.append( generateWeekdayNumber(weekdays) )
    return weekdays
    
def generateClassNumber(classes: list) -> str:
    classCode = ''
    for i in range (8):
        classCode += str( random.randrange(0, 2) )
    
    if classCode in classes: generateClassNumber(classes) 
    return classCode

def generateClasses(quantityOfClasses: int) -> list:
    classes = []
    for i in range(quantityOfClasses):
        classes.append( generateClassNumber(classes) )
    return classes
    
