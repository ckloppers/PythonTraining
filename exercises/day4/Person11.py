import random

class Person(object):
    """Person class"""

    def __init__(self, initName='Bruce', initAge=0):
        """ Class constructor """
        self.setName(initName)
        self.setAge(initAge)

    def __del__(self):
        """ Method destructor """
        print 'Im not dead yet'


    # Overloaded methods
    def __str__(self):
        """ toString method """
        return self.name

    def __cmp__(self, other):
        """ Sort based on Age """
        return cmp(self.age, other.age)

    # Property Methods
    @property
    def home(self):
        self._home

    def setName(self, newname):
        """Set the person class name"""
        self.name = newname

    def getName(self):
        """Get the person class name property"""
        return self.name

    def setAge(self, newAge):
        try:
            int(newAge)
        except:
            raise TypeError

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
        """ """
        print self.name + ' is ' + str(self.age)

    def nickName(self):
        if len(self.name) < 5:
            nick = ['o', 'y']
            return self.name + nick[random.randint(0,1)]
        else:
            return self.name[:4]

if __name__ == '__main__':
    p = Person()
    p.setName('Sam')
    p.setAge('10')

    x = Person()
    x.setAge(20)

    print 'Age compare:',cmp(p,x)

    #p.happyBirthday()

    print 'You are now:', p.getAge()
    p.display()

    print 'nick name:', p.nickName()
