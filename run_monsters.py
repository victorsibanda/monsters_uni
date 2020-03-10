from monsters_class import *
from students_class import *
from teacher_class import *
from monster_workshops import *
print('____________________________________________________________')
print('Welcome to Monster University')
print('____________________________________________________________')

list_of_attendees = []
list_of_teachers = []
list_of_students = []
workshops_list = []
student_id = 0
staff_id = 0

while True:
    user_input = ''
    user_input = input('Choose your option? \n 1: Add Student \n 2: Add Teacher \n 3: Add Workshop \n 4: Add Skill to '
                       'Student \n 5: Add name to list of Attendees \n')

    if user_input == '1':
        print('Adding a New Student')



        while user_input != 'quit':

            student_id += 1

            first_name = input('First Name:')
            last_name = input('Last Name:')
            student = Students(first_name, last_name,student_id)


            list_of_students.append(student)
            print(f'student name:  {list_of_students[-1].f_name} {list_of_students[-1].l_name}', f'Student_ID : {list_of_students[-1].student_id}')
            print("Number of students in list:" + str(len(list_of_students)))
            user_input = input('Do you want to continue or quit:')
            continue

    elif user_input == '2':
        print('Adding a New Teacher')




        while user_input != 'quit' :
            staff_id += 1

            first_name = input('First Name:')
            last_name = input('Last Name:')
            teacher = Teachers(first_name, last_name, staff_id)


            list_of_teachers.append(teacher)
            print(f'teacher name: {list_of_teachers[-1].f_name} {list_of_teachers[-1].f_name}', f'Staff_ID : {list_of_teachers[-1].staff_id}')
            print("Number of teachers in list:" + str(len(list_of_teachers)))
            user_input = input('Do you want to continue or quit:')
            continue

    elif user_input == '3':
        print('Adding Workshop')

        while user_input != 'quit':

            subject = input('What is the subject?')

            teacher_name = input('What is the teachers name?')

            workshop = Monster_workshop(subject,teacher_name)

            workshops_list.append(workshop)
            print(f'Subject: {workshops_list[-1].subject} ', f'Teacher Name: {workshops_list[-1].teacher}')
            user_input = input('Do you want to continue or quit:')

            continue

    elif user_input == '4':
        print('Add Skill to Student')
        # while loop
        while user_input != 'quit':
            # # student = int(input('what is the student ID:'))
            # # student.skills.append(skill)
            # for i in list_of_students:
            #     i.skills.append(skill)
            stud_id = int(input('what is the Student ID')) - 1
            new_skill = input('What is the skill you want to add')
            list_of_students[stud_id].skills.append(new_skill)

            print('Student skill: ', list_of_students[stud_id].skills, 'Student name: ', list_of_students[stud_id].f_name)

            user_input = input('Continue or quit:')
            continue
    elif user_input == '5':

        workshopID = int(input('What is the workshop ID'))-1
        attendant = input('Who is attending')
        list_of_attendees.append(attendant)
        #workshops_list[workshopID].append(list_of_attendees)
    else:
        print('please enter 1, 2, 3, or 4')


