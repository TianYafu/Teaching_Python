class BInode:
    def __init__(self,num,name,grade,leftchild,rightchild):
        self.num = num
        self.name = name
        self.grade = grade
        self.leftchild = leftchild
        self.rightchild = rightchild
    def __str__(self):
        return "N0.%s,Name %s,Grade,%s"  %(self.num,self.name,self.grade)

emptynode = BInode(0,"Null",0,"Null","Null")
BItree = []

Names = ["Peter","Jason","Tom","Ruby","Python","Jerry","Eve","Rxy","Jack"]
grades = [89,90,78,89,87,89,78,97,67]

for i,j in enumerate(Names):
    BItree.append(BInode(i,j,grades[i],emptynode,emptynode))

for i in BItree:
    print i

guanxi = [[1,2,3],[2,4,5],[3,6,7],[5,"e",8],[8,"e",9]]

for i in guanxi:
    if i[1] != "e":
        BItree[i[0] - 1].leftchild = BItree[i[1] - 1]
    else:
        BItree[i[0] - 1].leftchild = emptynode
    if i[2] != "e":
        BItree[i[0] - 1].rightchild = BItree[i[2] - 1]
    else:
        BItree[i[0] - 1].leftchild = emptynode

for i in BItree:
    print i.name
    print i.leftchild.name
    print i.rightchild.name
    print "##########################"

