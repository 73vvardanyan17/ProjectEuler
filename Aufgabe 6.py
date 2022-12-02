liste=[]
listesrq=[]
summe=0
summesqr=0

for y in range(1,101):
    if y>0:summesqr=y*y+summesqr


for i in range(1,101):
    if i>0:
        summe+=i
print((summe*summe)-(summesqr))


