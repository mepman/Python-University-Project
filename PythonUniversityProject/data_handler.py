import json
import os

data_file = r"D:\MEPMAN1\programming\hints_programming\python\codes\maktab_sharif\Uni\data.json"

# data_file = "data.json"


def load_data(selected_uni):
    """Loads data from the JSON file."""
    if not os.path.exists(data_file):
        return {"students": [], "teachers": [], "classes": []}

    with open(data_file, "r") as file:
        return json.load(file)


def save_data(class_name, selected_uni, input_type):
    """Saves data to the JSON file."""
    if not os.path.exists(data_file):
        dict = {selected_uni: {"students": [], "teachers": [], "classes": []}}
        dict[selected_uni][input_type].append(class_name)
        json_object = json.dumps(dict, indent=4)
        with open(data_file, "w") as file:
            file.write(json_object)
        return dict
    else:
        with open(data_file, "r") as file:
            dict = json.load(file)
            if selected_uni not in dict:
                dict[selected_uni] = {"students": [],
                                      "teachers": [], "classes": []}
            if class_name in dict[selected_uni][input_type]:
                print("Data already exists")

            else:
                dict[selected_uni][input_type].append(class_name)
                json_object = json.dumps(dict, indent=4)
                with open(data_file, "w") as file:
                    file.write(json_object)
                return dict
