class Person(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def print_title(self):
        if self.sex == "male":
            print("man")
        elif self.sex == "female":
            print("woman")


class Child(Person):  # Child 继承 Person
    def print_title(self):
        if self.sex == "male":
            print("boy")
        elif self.sex == "female":
            print("girl")


May = Child("May", "female")
Peter = Person("Peter", "male")

print(May.name, May.sex, Peter.name, Peter.sex)
May.print_title()
Peter.print_title()