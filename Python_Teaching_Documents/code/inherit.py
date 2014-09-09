# -*- coding: UTF-8 -*-
class Fruit:
    def __init__(self,color,shape):
        self.color = color
        self.shape = shape
    def grow(self):
        print "grow"

class Apple(Fruit):
    def __init__(self,color,taste):
        Fruit.__init__(self,color)
        self.taste = taste
        print "This Apple tastes %s"  %(self.taste)

##apple1 = Apple("green","sour")
##apple1.grow()

class Banana(Fruit):
    def __init__(self):
        self.color = "Yellow"

##banana1 = Banana()
##
##class Banaple(Banana,Apple):
##    def eat(self):
##        print "It tastes %s" %(self.taste)  #不调用的时候不报错
##
##class Appnana(Apple,Banana):
##    pass
##
##banaple1 = Banaple()
###banaple2 = Banaple("Red","Sweet")
##
##appnana1 = Appnana("Red","Sweet")
###appnana2 = Appnana()
