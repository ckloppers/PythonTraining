import Person3 as person

class Employee(person.Person):

    def __init__(self, startSalary=0):
        super(Employee, self).__init__()
        self._salary = startSalary

    def setSalary(self, newSalary):
        self._salary = newSalary

    def getSalary(self):
        return self._salary

    def giveRaise(self, amount):
        self.setSalary(self.getSalary() + amount)
        # self._salary = self._salary + amount

# start of pro
e = Employee(100)
e.giveRaise(50)

print 'Salary after raise:', e.getSalary()
print 'Name:', e.getName()

