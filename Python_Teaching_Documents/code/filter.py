list1 = []
for i in range(10):
    list1.append((i**2)+2*i+1)

print list1

def mod3(x):
    return (x%3 != 0)

list2 = filter(mod3,list1)
print list2

list3 = filter(lambda x:x%3 != 0,list1)
print list3
