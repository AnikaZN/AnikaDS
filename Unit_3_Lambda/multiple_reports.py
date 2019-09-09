import random
from admissions import Student

def summary_multiple(n):
    names = []
    while n > 0:
        x = input('Student Name:' )
        names.append(x)
        n = n-1

    for name in names:
        example = Student(name)
        report = example.summary()

    return report

summary_multiple(4)
