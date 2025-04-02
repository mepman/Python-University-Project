from cls import cls
from uni import Uni
from data_handler import load_data


def display_main_menu():
    menu = '''
    1. Oxford
    2. Dubai
    3. Exit
'''
    return menu


def processing(selected_uni):
    uni = Uni()
    print(display_uni_menu())
    user_input = input('Please enter a number: ')
    cls()
    if int(user_input) == 1:
        class_name = input('Please enter class name: ')
        uni.sign_up_class(class_name, selected_uni)
        input('You have successfully signed up for the class. Press any key to continue...')
        cls()

    if int(user_input) == 2:
        teacher_name = input('Please enter teacher name: ')
        data = uni.sign_up_teacher(teacher_name, selected_uni)
        input('You have successfully signed up for the teacher. Press any key to continue...')
        cls()

    if int(user_input) == 3:
        student_name = input('Please enter student name: ')
        data = uni.sign_up_student(student_name, selected_uni)
        input('You have successfully signed up for the student. Press any key to continue...')
        cls()

    if int(user_input) == 4:
        loaded_data = uni.total_stuffs()
        students_count, teachers_count, classes_count = map(
            len, (loaded_data[selected_uni][key] for key in ['students', 'teachers', 'classes']))
        print(
            f"Category   | Count\n{'-' * 20}\nStudents   | {students_count}\nTeachers   | {teachers_count}\nClasses    | {classes_count}")
        input('Press any key to continue...')
        cls()
    if int(user_input) == 5:
        loaded_data = load_data(selected_uni)
        print(loaded_data[selected_uni])
        input('Press any key to continue...')

    cls()


def display_uni_menu():
    menu = '''
            1. Sign Up Class
            2. Sign Up Teacher
            3. Sign Up Student
            4. Total Classes, Teachers, and Students
            5. Total Classes, Teachers, and Students Lists
            any other key to exit.
                            '''
    return menu


def main():
    print(display_main_menu())
    user_input = input('Please enter your choice: ')
    cls()
    if int(user_input) == 1:
        selected_uni = 'Oxford'
        processing(selected_uni)
        cls()

    elif int(user_input) == 2:
        selected_uni = 'Dubai'
        processing(selected_uni)
        cls()
    elif int(user_input) == 3:
        exit()
    cls()
    main()


if __name__ == "__main__":
    main()




# /your_project/
# │── main.py          # Entry point
# │── uni.py           # Uni class
# │── data_handler.py  # Handles saving/loading data
# │── cls.py           # Function to clear console
# │── data.json        # Stores student, teacher, course info
# │── README.md        # Project documentation
