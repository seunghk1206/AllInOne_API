import math

a = 0
for x in range(10000000):#10^100
    a += ((-1)**(x))*1/(2*x+1)

print(4*a)
#3.14159265359
#3.1415925535897915
#3.1415916535897743