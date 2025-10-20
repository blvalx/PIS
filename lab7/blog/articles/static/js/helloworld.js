var groupmates = [
    {
        "name": "Александр",
        "surname": "Бубнов",
        "group": "БСТ2203",
        "marks": [5,4,5]
    },
    {
        "name": "Леонид",
        "surname": "Каневский",
        "group": "БСТ2201",
        "marks": [3,3,4]
    },
    {
        "name": "Федор",
        "surname": "Потапов",
        "group": "БСТ2202",
        "marks": [3,5,4]
    },
    {
        "name": "Прохор",
        "surname": "Шаляпин",
        "group": "БСТ2201",
        "marks": [5,5,5]
    },
    {
        "name": "Ксения",
        "surname": "Самосвалова",
        "group": "БСТ2204",
        "marks": [3,3,3]
    },
];

var rpad = function(str, length) {
// js не поддерживает добавление нужного количества символов
// справа от строки, т.е. аналога ljust из Python здесь нет
    str = str.toString(); // преобразование в строку
    while (str.length < length)
        str = str + ' '; // добавление пробела в конец строки
        return str; // когда все пробелы добавлены, возвратить строку
};

var printStudents = function(students) {
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
// был выведен заголовок таблицы
    for (var i = 0; i<=students.length-1; i++){
    // в цикле выводится каждый экземпляр студента
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n'); // добавляется пустая строка в конце вывода
};

printStudents(groupmates);

// Фильтрация по группе
var groupName = prompt("Введите название группы: ");
var filterByGroup = function(students, groupName) {
    console.log('Фильтрация по группе: ' + groupName);
    printStudents(students.filter(student => student.group === groupName));
}
filterByGroup(groupmates, groupName);

// Фильтрация по среднему баллу
var inputAvgMark = parseFloat(prompt("Введите средний балл: ").replace(',', '.'));

var avgMark = function(marks) {
    let sum = marks.reduce((acc, val) => acc + val, 0);
    return sum / marks.length;
}

var filterByMarks = function(students, avgMarkValue) {
    console.log('Фильтрация по среднему баллу > ' + avgMarkValue);
    printStudents(students.filter(student => avgMark(student.marks) > inputAvgMark));
}
filterByMarks(groupmates, inputAvgMark);
