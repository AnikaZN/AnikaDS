import random

#create a function called "Summary" giving all info on Student
#automatically generate multiple students, create a bigger report
#practice the git push workflow


class Student():
    def __init__(self, name, age = 1,
                precourse_scores = 1,
                passing_score = 3.5, applied = 'yes'):
        self.name = name
        self.age = random.randint(18, 56)
        self.precourse_scores = random.sample(range(1, 6), 5)
        self.passing_score = passing_score
        self.applied = applied

    def results(self):
        total = sum(self.precourse_scores)
        mean = (total/5)
        if mean < 2.0:
            return(mean, 'Could never be a Data Scientist')
        elif mean > 2.0 and mean < 3.5:
            return(mean, 'Might be a Data Scientist')
        elif mean > 3.5 and mean < 4.5:
            return(mean, 'Data Scientist material')
        else:
            return(mean, 'Student will make us a lot of money')

    def accepted(self):
        total = sum(self.precourse_scores)
        mean = (total/5)
        if mean > self.passing_score:
            print('Yes')
        else:
            print('No')

    def summary(self):
        sample = Student('Anika')
        print('---SUMMARY---')
        print('Applicant Name:', self.name)
        print('Applicant Age:', self.age)
        print('Precourse Scores:', self.precourse_scores)
        print('Results:', sample.results())
        print('Accepted:', sample.accepted())
