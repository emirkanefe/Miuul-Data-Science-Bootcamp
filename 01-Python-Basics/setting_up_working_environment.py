from functools import reduce

students = ["a","b","c","d","e"]


def divide_students(students):
    groups = [[],[]]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

divide_students(students)


def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)


alternating_with_enumerate("Selam ben emirkan.")

new_sum = lambda a, b: a + b

new_sum(1,3)

salaries = [1,2,3,4,5,6,7,8,9]

list_store= [1,2,3,4]
(lambda a,b: a+b, list_store)
reduce((lambda a,b: a+b, list_store))
