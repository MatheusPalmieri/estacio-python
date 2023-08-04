class Person:
    def __init__(self, name, age):
        self.set_name(name)
        self.set_age(age)

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Job(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job

    def print_person(self):
        print(
            f'My name is {self.get_name()} and I am {self.get_age()} years old, and I work as a {self.job}')


person01 = Job('Matheus', 19, 'Software Engineer')
person02 = Job('André', 25, 'IT Support')

person01.print_person()
person02.print_person()
