class Student:

    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return round(self.qpoints/self.hours, 2)

    def addGrade(self, gradePoint, credits):
        gradePoint = gradePoint
        credits = credits
        qpoints = float(gradePoint * credits)
        self.hours = float(self.hours + credits)
        self.qpoints = float(self.qpoints + qpoints)


def makeStudent(name, hours, qpoints):
    name, hours, qpoints = name, hours, qpoints
    return Student(name, hours, qpoints)

def main():

    name = str(input("Enter the incoming student's name: "))
    newStudent = makeStudent(name, 0, 0)
    print("Let's add some grades!")

    resp = ""

    while resp != "n":
        newGrade = float(input("Enter the grade point:  "))
        newCredits = float(input("How many credits is this class?  "))
        newStudent.addGrade(newGrade, newCredits)
        resp = str(input("Would you like to add another? Type y/n "))

    print(str(newStudent.name) + "'s GPA is: " + str(newStudent.gpa()))


main()
