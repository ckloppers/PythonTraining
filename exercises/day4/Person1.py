class Person:
    """Person class"""

    #Methods
    def setName(self, newname):
        """Set the person class name"""
        self.name = newname

    def getName(self):
        """Get the person class name property"""
        return self.name

p = Person()
p.setName('Corne')

print 'Name in class:', p.getName()