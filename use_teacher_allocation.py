from teacher_allocation import *
import time


def flow():
    gen = 0
    classroom = generateClassroom(8)
    weekdays = generateWeekdays(5)
    classes = generateClasses(33)
    population = inicialization(classroom, weekdays, classes)
    while 1 != 0:
        fitness(population)
        if finishing(population, gen):
            return population
        newPopulation = selection(population)
        excludedPopulation = excludedSelection(population)
        newPopulation = crossover(newPopulation)
        mutation(newPopulation)
        population = update(newPopulation, excludedPopulation, classroom, weekdays)
        gen += 1



flow()
