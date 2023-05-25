#!/usr/bin/env python3
'''Displays student report by activity.

Print the list of students grouped by room,
who attend each of the activities.
'''
__version__ = '0.1.0'
__author__ = 'https://github.com/edsaantos'
__license__ = 'Unlisence'

# Students by classroom
classroom_one = ['Andbay', 'Bugan', 'Caora', 'Cocuborn', 'Ellond', 'Elpen']
classroom_two = ['Fallvavuy', 'Gulus', 'Hami', 'Muli', 'Myuan']

# Students by activity
activity_ingles = ['Andbay', 'Gulus', 'Cocuborn', 'Myuan', 'Elpen']
activity_music = ['Andbay', 'Hami', 'Ellond']
activity_dance = ['Fallvavuy', 'Bugan', 'Caora', 'Muli',]

activities = [('Ingles', activity_ingles), ('Music', activity_music), ('Dance', activity_dance)]

# List students in each activity by room

for activity_name, activity in activities:
    
    print(f'Students enrolled in the {activity_name} activity in classrooms:')

    activity_classroom_one = []
    activity_classroom_two = []

    for student in activity:
        if student in classroom_one:
            activity_classroom_one.append(student)
        elif student in classroom_two:
            activity_classroom_two.append(student)

    print(f'C1:\n{activity_classroom_one}\n')
    print(f'C2:\n{activity_classroom_two}')

    print('-' * 30)