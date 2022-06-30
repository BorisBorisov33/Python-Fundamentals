from Objects_and_Classes.child_class import Child


class GrandChildClass(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def get_address(self):
        return self.address


test = GrandChildClass('Ivan Ivanov', 33, 'Sofia')
print(test.get_name(), test.get_age(), test.get_address())
