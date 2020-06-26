people = [
    {'name': 'John', "age": 64},
    {'name': 'Janet', "age": 34},
    {'name': 'Ed', "age": 24},
    {'name': 'Sara', "age": 64},
    {'name': 'John', "age": 32},
    {'name': 'John', "age": 99},
]


#sort by name AND age
import operator
people.sort(key=operator.itemgetter('age'))
people.sort(key=operator.itemgetter('name'))
print(people)
