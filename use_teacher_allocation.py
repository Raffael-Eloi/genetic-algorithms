from teacher_allocation import *
import time


def flow( population: list) -> list:
    gen = 0
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


classroom = generateClassroom(8)
weekdays = generateWeekdays(5)
classes = generateClasses(33)
population = inicialization(classroom, weekdays, classes)
flow(population)
