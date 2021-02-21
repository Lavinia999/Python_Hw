list=[30,4,15,62,34,97,45,1,34,21]
maxim = list[0]
for x in list:
    if x > maxim:
        maxim = x
minim = list[0]
for x in list:
    if x < minim:
        minim = x   
suma=0
for x in list:
    suma+=x