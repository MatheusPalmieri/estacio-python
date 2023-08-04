class Person:
    def __init__(self, name, address, age):
        self.set_name(name)
        self.set_address(address)
        self.set_age(age)

    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age


person01 = Person('Matheus', 'Rua Noruega, 840', 19)
person02 = Person('André', 'Rua México, 400', 25)

print(f'Meu nome eh {person01.get_name()}, tenho {person01.get_age()} e moro no endereço {person01.get_address()}.')
print(f'Meu nome eh {person02.get_name()}, tenho {person02.get_age()} e moro no endereço {person02.get_address()}.')
