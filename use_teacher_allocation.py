from teacher_allocation import *

classroom = generateClassroom(8)
weekdays = generateWeekdays(5)
classes = generateClasses(33)
print(classroom)
print(weekdays)
print(classes)

print('Population')
population = inicialization(classroom, weekdays, classes)
print(len(population))
#print('\n')
