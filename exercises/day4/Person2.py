class Person:
    """Person class"""

    # Property Methods
    def setName(self, newname):
        """Set the person class name"""
        self.name = newname

    def getName(self):
        """Get the person class name property"""
        return self.name

    def setAge(self, newAge):
        if newAge in range(0, 970):
            self.age = newAge
        elif newAge > 969:
            self.age = 969
        else:
            self.age = 0

    def getAge(self):
        return self.age

    # General methods
    def happyBirthday(self):
        self.age += 1

    def display(self):
        print self.name + ' is ' + str(self.age)

p = Person()
p.setName('Corne')
p.setAge(-15)

#p.happyBirthday()

print 'You are now:', p.getAge()
p.display()
