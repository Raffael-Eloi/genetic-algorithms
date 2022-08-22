from teacher_allocation import *

classroom = generateClassroom(8)
weekdays = generateWeekdays(5)
classes = generateClasses(33)
#print(classroom)

print('Population')
population = inicialization(classroom, weekdays, classes)
#print(population)
fitness(population)
#print(population)
selection = selection(population)
#print(population)
newPopulation = crossover(selection)
