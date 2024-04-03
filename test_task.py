import unittest

class Task:
    def solve_task(self, grades):
        persons = self.__get_unique_person_names(grades)

        average_grades = {}
        for person in persons:
            average_grades[person] = self.__get_average(grades, person)

        return average_grades

    def __get_average(self, grades, person):
        subjects = self.__map_subjects_by_person(grades, person)
        dict_subjects = self.__convert_subjects_to_dict(subjects)
        average_subjects = self.__get_subjects_average(dict_subjects)
        return average_subjects

    def __map_subjects_by_person(self, grades, person):
        subjects = []
        for grade in grades:
            if grade['name'] == person:
                subjects.append(self.__convert_subject(grade))
        return subjects

    def __convert_subjects_to_dict(self, subjects):
        subjects_dict = {}
        for subject in subjects:
            if subject['name'] in subjects_dict:
                subjects_dict[subject['name']].append(subject['grade'])
            else:
                subjects_dict[subject['name']] = [subject['grade']]

        return subjects_dict

    def __get_subjects_average(self, subjects):
        average_subjects = {}
        for subject_key, grades in subjects.items():
            average_subjects[subject_key] = self.__get_list_average(grades)

        return average_subjects

    def __get_list_average(self, list):
        sum = 0
        for elem in list:
            sum += elem

        return sum / len(list)

    def __get_unique_person_names(self, grades):
        person_names = []
        for grade in grades:
            person_names.append(grade['name'])

        return set(person_names)


    def __convert_subject(self, grade):
        converted_subject = {
            'name': grade['subject'],
            'grade': grade['grade']
        }
        return converted_subject


class TestTask(unittest.TestCase):
    task = Task()
    grades = [
        {'name': 'Ася', 'subject': 'math', 'grade': 1},
        {'name': 'Ася', 'subject': 'math', 'grade': 4},
        {'name': 'Ася', 'subject': 'history', 'grade': 1},
        {'name': 'Борис', 'subject': 'math', 'grade': 5},
        {'name': 'Борис', 'subject': 'math', 'grade': 3},
        {'name': 'Борис', 'subject': 'programming', 'grade': 3},
        {'name': 'Владимир', 'subject': 'biology', 'grade': 4}
    ]

    def test_task(self):
        simple_grades = self.task.solve_task(self.grades)

        expected = {
            'Ася': {
                'math': 2.5,
                'history': 1
            },
            'Борис': {
                'math': 4,
                'programming': 3
            },
            'Владимир': {
                    'biology': 4,
            }
        }

        self.assertEqual(expected, simple_grades)


