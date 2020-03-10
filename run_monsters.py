from monsters_class import *
from students_class import *
from teacher_class import *
from monster_workshops import *

while True:
    user_input = ''
    user_input = input('choose your option? 1: Add Student \n 2: Add Teacher \n 3: Add Workshop \n 4: Add Skill to '
                       'list \n 5:Add skill to student')
    if user_input == '1':
        list_of_students = []
        student_id = 0

        while user_input != 'quit':

            student_id += 1

            first_name = input('First Name:')
            last_name = input('Last Name:')
            student = Students(first_name, last_name,student_id)


            list_of_students.append(student)
            print(f'student name: {first_name} {last_name}', f'Student_ID : {student_id}')
            print("Number of students in list:" + str(len(list_of_students)))
            user_input = input('Do you want to continue or quit:')
            continue


    elif user_input == '2':
        list_of_teachers = []

        staff_id = 0



        while user_input != 'quit' :
            staff_id += 1

            first_name = input('First Name:')
            last_name = input('Last Name:')
            teacher = Teachers(first_name, last_name, staff_id)


            list_of_teachers.append(teacher)
            print(f'teacher name: {first_name} {last_name}', f'Staff_ID : {staff_id}')
            print("Number of teachers in list:" + str(len(list_of_teachers)))
            print (list_of_teachers[0].f_name)
            user_input = input('Do you want to continue or quit:')
            continue


#With every iteration of while loop ask for user input
#Create student from inputs
#Have a student ID Counter

    elif user_input == '3':
# As a Receptionist of the University, I should be able to create a workshop
# create a list for workshops

        workshops_list =  []
# while loop
        while user_input != 'quit':

    # ask for subject
            subject = input('What is the subject?')
    # ask for list of attendants
            list_of_attendants = input('Who are the attendees?')
    # ask for teacher name
            teacher_name = input('What is the teachers name?')

            workshop = Monster_workshop(subject,teacher_name)

# adding workshop to list of workshops
            workshops_list.append(workshop)
            print(f'Subject: {subject} ', f'Teacher Name: {teacher_name}')
            user_input = input('Do you want to continue or quit:')
            continue
    elif user_input == '4':

        skill_list = []
# while loop
        while user_input != 'quit':

            skill = input('What is the skill?')
    # ask for list of attendants
    # ask for teacher name

            skill_list.append(skill)
            print(f'Skill: {skill} ')
            user_input = input('Do you want to continue or quit:')
            continue
    elif user_input == '5':

        # while loop
        while user_input != 'quit':
            for i in list_of_students:
                i.skills.append(skill_list)

            print(student.skills)

            user_input = input('Continue or quit:')
            continue
    else:
        print('please enter 1 , 2 or 3')
        user_input = input('?')




#if student is in list
# add skill to student in list
