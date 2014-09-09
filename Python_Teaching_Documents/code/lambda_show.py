print (reduce(lambda x,y:x*y,range(1,101)))

print (filter(lambda x:x%2 != 0,range(1,101)))

print [x for x in range(1,100) if not [y for y in range(2,x/2+1)if x % y == 0]] 
