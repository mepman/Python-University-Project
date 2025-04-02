from data_handler import save_data, load_data


class Uni():
    def __init__(self, uni_name=2, class_name=5, uni_id=1):
        pass
    def sign_up_class(self, class_name, selected_uni):
        input_type = 'classes'
        dict_data = save_data(class_name, selected_uni, input_type)
        return dict_data

    def sign_up_teacher(self, teacher_name, selected_uni):
        input_type = 'teachers'
        dict_data = save_data(teacher_name, selected_uni, input_type)
        return dict_data

    def sign_up_student(self, student_name, selected_uni):
        input_type = 'students'
        dict_data = save_data(student_name, selected_uni, input_type)
        return dict_data

    def total_stuffs(self):
        data = load_data()
        return data

    def uni_id(self):
        pass
