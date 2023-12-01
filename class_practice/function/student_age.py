student_dict = dict({"dike": 33, "ope": 25, "melody": 20, "precious": 27})
global age


def student_name_and_age():
    global age

    name = input("Enter the student name: ").lower()
    for student_name in student_dict.keys():
        if name == student_name:
            return f"{name}, your age is {student_dict.get(student_name)}"
    else:
        while name not in student_dict.keys():
            age = int(input("Name not found enter your age: "))
            student_dict.update({name: age})

            return f"Hi, {name}, you are {student_dict.get(name)} years old"


# print(student_name_and_age())
# print(student_dict)


def student_name_and_age_(name: str, age: int):

    name.lower()
    for student_name in student_dict.keys():
        if name == student_name:
            return f"{name}, your age is {student_dict.get(student_name)}"
    else:
        while name not in student_dict.keys():
            # age = int("Name not found enter your age: ")
            student_dict.update({name: age})

            return f"Hi, {name}, you are {student_dict.get(name)} years old"


print(student_name_and_age_("odey", 23))
print(student_dict)
