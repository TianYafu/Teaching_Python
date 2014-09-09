class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "My name is %s,I'm %s years old"  %(self.name,self.age)
    def hello(self):
        print "hello~~~~~"
    def __and__(self,other):
        return "%s and %s" %(self.name,other.name)
    def __mul__(self,other):
        return self.age * other.age

tom = People("Tom",18)

print tom.name
print tom.age
print tom

class Student(People):
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        self.school = school
    def __str__(self):
        return "I'm in %s school"  %(self.school)
    def __call__(self,word):
        if (word == "name"):
            return self.name
        if (word == "age"):
            return self.age
        if (word == "school"):
            return self.school

jerry = Student("Jerry",18,"No.1 Primary")

jerry.hello()

class Monitor(Student):
    def hello1(self):
        return "Waaaaaaaaaaaaaaaaaaaaaagh"

jason = Monitor("Student",21,"No.2")

class Man(People):
    sex = "Boy"

class Woman(People):
    sex = "Girl"
    def __add__(self,other):
        return "%s,and %s" %(self.name,other.name)
    def __gt__(self,other):
        if self.age > other.age:
            return True
        else:
            return False
    def __ge__(self,other):
        if self.age >= other.age:
            return True
        else:
            return False

marry = Woman("Marry",17)
Jason = Woman("Jason",18)

class indexer:
    def __init__(self,name):
        self.name = name
    def __getitem__(self,index):
        return index**2 + 2*index +1
    def __len__(self):
        return 5



a = indexer(1)



