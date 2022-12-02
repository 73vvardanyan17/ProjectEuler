liste=[]
import math, time
start=time.time()

def prime(x):
    for i in range(2,int(math.sqrt(x)+1)):
        if (x%i==0):
            return False
    return True

for x in range(1,104743+1):
    if prime(x):
        liste.append(x)

print(liste[10001])

end_time=time.time()

print(end_time-start)