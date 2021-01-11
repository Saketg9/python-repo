class Student():

    def __init__(self, firstname="unspecified", lastname="unknown", age="unknown", gender="unknown", course="unknown"):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.course = course
        print('Hi I am', self.firstname , 'my surname is', self.lastname , 'I am' , self.age , 'I am a', self.gender , 'the course I am attending is', self.course)


student1 = Student("Saket", "Ghai", "27", "Male", "Computer Science")