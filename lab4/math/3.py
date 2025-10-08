import math
number = int(input())
length = int(input())
area = (number*length**2)/(4*(math.tan(math.pi/number)))
print(area)
