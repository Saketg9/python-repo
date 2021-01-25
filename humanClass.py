class Human():
    def __init__(self, name="unknown", age="unknown", gender="unknown"):
        self.name = name
        self.age = age
        self.gender = gender
        print('My name is', self.name , 'I am', self.age , 'I am a', self.gender)

class Student(Human):
    def __init__(self, name="unknown", age="unknown", gender="unknown", year=None, uni='Queen Mary'):
        Human.__init__(self, name, age, gender)
        self.year = year
        self.uni = uni
        print('student year number is' , self.year, 'My university is' , self.uni)
    


student1 = Student('Saket', '27', 'male', 10, 'Queen Mary')
