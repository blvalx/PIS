groupmates = [
    {
        "name": "Александр",
        "surname": "Бубнов",
        "exams": ["АИС","Философия","ВышМат"],
        "marks": [5,4,5]
    },
    {
        "name": "Леонид",
        "surname": "Каневский",
        "exams": ["Физкультура","ППСУБДиЗ","АИС"],
        "marks": [3,3,4]
    },
    {
        "name": "Федор",
        "surname": "Потапов",
        "exams": ["История","Русский язык","ППСУБДиЗ"],
        "marks": [3,5,4]
    },
    {
        "name": "Прохор",
        "surname": "Шаляпин",
        "exams": ["Экономика","Правоведение","История"],
        "marks": [5,5,5]
    },
    {
        "name": "Ксения",
        "surname": "Самосвалова",
        "exams": ["ОС","Экономика","Физкультура"],
        "marks": [3,3,3]
    },
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(15), u"Экзамены".ljust(40), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(15), str(student["exams"]).ljust(40), str(student["marks"]).ljust(20))
print_students(groupmates)

x = float(input("\nВведите средний балл: "))
def avg(students, x):
    print(u"\nИмя".ljust(16), u"Фамилия".ljust(15), u"Экзамены".ljust(40), u"Оценки".ljust(20), u"Средний балл".ljust(5))
    for student in students:
        avg = sum(student["marks"])/ len(student["marks"])
        if avg >= x:
            print(student["name"].ljust(15), student["surname"].ljust(15), str(student["exams"]).ljust(40), str(student["marks"]).ljust(20), str(round(avg,2)).ljust(5))
avg(groupmates, x)

