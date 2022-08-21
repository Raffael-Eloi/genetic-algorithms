from teacher_allocation import *

print('All the classsroom')
classroom = generateClassroom(8)   
print(classroom)   
print('\n')

print('All the weekdays')
weekdays = generateWeekdays(5)   
print(weekdays)   
print('\n')

print('All the classes')
classes = generateClasses(33)   
print(classes)   
print('\n')

print('Population')
population = inicialization(classroom, weekdays, classes)
print('\n')
