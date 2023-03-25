class Student:
    def __init__(self, student_id, first_name, last_name):
        '''Конструктор класса'''
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.exam_scores = []
    def __str__(self):
        return f'{self.first_name.title()} {self.last_name.title()}'

    def add_score(self, score:float):
        '''Добавление оценки'''
        self.exam_scores.append(score)

    def show_scores(self):
        '''Отобразить все оценки'''
        for exam_score in self.exam_scores:
            print(exam_score, end=', ')

    def score_average(self):
        '''Средний балл оценок или информирование о том, что нет сданных экзаменов'''
        total_points = 0
        for exam_score in self.exam_scores:
            total_points += exam_score
        if total_points != 0:
           average_score = total_points / len(self.exam_scores)# По идее, доп.перем тут не нужна
           return f"\n{total_points / len(self.exam_scores)}"
        else:
           return f"Вы ещё не сдали ни одного экзамена"

    def course_passed(self):
        '''Информация о том, пройден ли курс'''
        total_points = 0
        for exam_score in self.exam_scores:
            total_points += exam_score
        average_score = total_points / len(self.exam_scores)
        if average_score > 60:
            return True
        else:
            return False

'''Создаю экземпляр ученика'''
kate_violin = Student(1, 'ekaterina', 'violin')
'''Вывожу экземпляр ученика, используя магический метод'''
print(kate_violin)
'''Добавляю оценку ученику в атрибут score'''
kate_violin.add_score(25.5)
kate_violin.add_score(13.5)
kate_violin.add_score(55.5)
'''Отображаю оценки студента'''
kate_violin.show_scores()
'''Вывожу средний балл, либо информирую об отсутствии сданных экзаменов'''
print(kate_violin.score_average())
'''Уточняю, пройден ли курс.'''
print(kate_violin.course_passed())