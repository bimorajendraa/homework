class Student():

    # constructor
    def __init__(self, name, birthday, faculty):
        self.name = name
        self.birthday = birthday
        self.faculty = faculty
    
    def attend_class(self, subject):
        print("{0} is attending {1} class".format(self.name, subject))

john = Student(name="John", birthday="26/04/2000", faculty="Science")
dewi = Student(name="Dewi", birthday="29/05/1998", faculty="Computer science")

print(john.faculty)
print(dewi.birthday)

dewi.attend_class("Python for data")