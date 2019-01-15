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
    pass


May = Child("May", "female")
Peter = Person("Peter", "male")

print(May.name, May.sex, Peter.name, Peter.sex)  # 子类继承父类方法及属性
May.print_title()
Peter.print_title()