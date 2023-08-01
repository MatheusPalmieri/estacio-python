# primeiro exemplo
from operator import attrgetter
import collections
import operator
from functools import partial
add_one = partial(operator.add, 1)

print(add_one(5))

# segundo exemplo
person = collections.namedtuple('person', 'name age')
persons = [
    person('Matheus', 19),
    person('João', 40),
    person('Renata', 26),
]

print(f'\n{sorted(persons, key = attrgetter("name"))}')
print(f'{sorted(persons, key = attrgetter("age"))}')

# terceiro exemplo
sort_name = partial(sorted, key=attrgetter('name'))
sort_age = partial(sorted, key=attrgetter('age'))

print(f'\n{sort_name(persons)}')
print(f'{sort_age(persons)}')
