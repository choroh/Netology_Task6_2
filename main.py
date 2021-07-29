#  Netology. Задача 6.2

#  класс Mentor должен стать родительским классом, а от него нужно реализовать наследование классов
#  Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания).

#  Реализуйте метод выставления оценок лекторам у класса Student (оценки по 10-балльной шкале,
#  хранятся в атрибуте-словаре у Lecturer, в котором ключи – названия курсов, а значения – списки оценок).
#  Лектор при этом должен быть закреплен за тем курсом, на который записан студент.

#  Перегрузите магический метод __str__ у всех классов.

#  Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции
#  и студентов по средней оценке за домашние задания.


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    #  Оценка лекторов учениками
    def lecturer_grade(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        self.avr_grade = 0  # Средняя оценка
        self.summa_grades = 0  # Сумма оценок
        self.finished_courses_str = 'Нет'
        self.courses_in_progress_str = 'Нет'
        #  Если есть оценки - посчитать среднюю
        if len(self.grades.values()) != 0:
            for i in self.grades.values():
                self.count_lecture = len(i)
                for j in i:
                    self.summa_grades += j
            self.avr_grade = self.summa_grades / self.count_lecture
        else:
            self.avr_grade = 0

        if self.finished_courses:
            self.finished_courses_str = ' '.join(self.finished_courses)
        if self.courses_in_progress:
            self.courses_in_progress_str = ' '.join(self.courses_in_progress)
        out = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avr_grade}\n' \
              f'Курсы в процессе изучения: {self.courses_in_progress_str}\nЗавершенные к' \
              f'урсы: {self.finished_courses_str} '
        return out

    def __lt__(self, other):
        return self.avr_grade < other.avr_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def __str__(self):
        self.avr_grade = 0
        self.summa_grades = 0

        #  Если есть оценки - посчитать среднюю
        if len(self.grades.values()) != 0:
            for i in self.grades.values():
                self.count_lecture = len(i)
                for j in i:
                    self.summa_grades += j
            self.avr_grade = self.summa_grades / self.count_lecture
        else:
            self.avr_grade = 0
        #  Вывести в заданном формате
        out = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avr_grade}'
        return out

    def __lt__(self, other):
        return self.avr_grade < other.avr_grade


class Reviewer(Mentor):
    def __init__(self, name, surname):  # Создание объекта
        super().__init__(name, surname)  # Привязка к параметрам родительского класса

    def __str__(self):  # Переопределение вывода
        out = f'Имя: {self.name}\nФамилия: {self.surname}'
        return out


#  Студенты
pushkin = Student('Александр', 'Пушкин', 'm')
lermontov = Student('Юрий', 'Лермонтов', 'm')
gogol = Student('Николай', 'Гоголь', 'm')

# Предметы изучаемые студентами
pushkin.courses_in_progress += ['Python']
lermontov.courses_in_progress += ['C#']
gogol.courses_in_progress += ['Python']

#  Завершенные курсы
pushkin.finished_courses += ['Git']
lermontov.finished_courses += ['Git']

#  Эксперты
tesla = Reviewer('Никола', 'Тесла')
isaak = Reviewer('Исаак', 'Ньютон')
bor = Reviewer('Нильс', 'Бор')

#  Предметы экспертов
tesla.courses_attached += ['Python']
isaak.courses_attached += ['C#']
#  bor.courses_attached += ['PHP']

#  Лекторы
nikulin = Lecturer('Юрий', 'Никулин')
morgunov = Lecturer('Евгений', 'Моргунов')

#  Предметы лекторов
nikulin.courses_attached += ['Python']
morgunov.courses_attached += ['C#']

#  Оценка студентов эеспертами
tesla.rate_hw(pushkin, 'Python', 9)
isaak.rate_hw(lermontov, 'C#', 8)
tesla.rate_hw(pushkin, 'Python', 10)

#  Оцентка лекторов студентами
pushkin.lecturer_grade(nikulin, 'Python', 10)
gogol.lecturer_grade(nikulin, 'Python', 8)
lermontov.lecturer_grade(morgunov, 'C#', 10)

#  Вывод студентов
print('Студенты:')
print(pushkin)
print('')
print(lermontov)
print('')
print(gogol)
print('----------')

#  Сравнение студентов
print('Сравнение студентов')
if pushkin < lermontov:
    print(f'{pushkin.name} {pushkin.surname} имеет менее высокий бал чем {lermontov.name} {lermontov.surname}')
else:
    print(f'{pushkin.name} {pushkin.surname} имеет более высокий бал чем {lermontov.name} {lermontov.surname}')
print('----------')

#  Вывод лекторов
print('Лекторы:')
print(nikulin)
print('')
print(morgunov)
print('----------')

#  Сравнение лекторов
print('Сравнение лекторов')
if nikulin < morgunov:
    print(f'{nikulin.name} {nikulin.surname} имеет менее высокий бал чем {morgunov.name} {morgunov.surname}')
else:
    print(f'{nikulin.name} {nikulin.surname} имеет более высокий бал чем {morgunov.name} {morgunov.surname}')
print('----------')

#  Вывод экспертов
print('Эксперты:')
print(tesla)
print('')
print(isaak)
print('')
print(bor)
