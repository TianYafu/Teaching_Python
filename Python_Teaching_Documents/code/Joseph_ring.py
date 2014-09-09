def Joseph(n,m):
    circle=[x + 1 for x in range(n)]
    curve = 0
    result = []
    while len(circle):
        curve = ( curve + m - 1) % len(circle)
        result.append(circle.pop(curve))
    return result

n = input("The number of people\n")
m = input("show me the code\n")
print Joseph(n,m)
