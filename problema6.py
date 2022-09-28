import math
x=int(input("Dati primul nr: "))
y=int(input("Dati al doilea  nr: "))
z=int(input("Dati al treilea nr: "))  
k=int(input("Dati al patrulea nr: "))  

#1
def triunghiuri(a,b,c,d):
    if (a+b>c) and (a+c>b) and (b+c>a):
        sp=(a+b+c)/2
        aria=round(math.sqrt(sp*(sp-a)*(sp-b)*(sp-c)),3)
        perimetru=sp*2
        return print("Laturile",a,',',b,',',c, "pot forma un triunghi, astfel aria acestuia va fi: ",aria,", iar perimetrul: ",perimetru)
    elif (a+b>d) and (a+d>b) and (b+d>a):
        sp=(a+b+d)/2
        aria=round(math.sqrt(sp*(sp-a)*(sp-b)*(sp-d)),3)
        perimetru=sp*2
        return print("Laturile",a,',',b,',',d, "pot forma un triunghi, astfel aria acestuia va fi: ",aria,", iar perimetrul: ",perimetru)
    elif (c+b>d) and (c+d>b) and (d+b>c):
        sp=(c+b+d)/2
        aria=round(math.sqrt(sp*(sp-c)*(sp-b)*(sp-d)),3)
        perimetru=sp*2
        return print("Laturile",c,',',b,',',d, "pot forma un triunghi, astfel aria acestuia va fi: ",aria,", iar perimetrul: ",perimetru)

    elif (c+a>d) and (c+d>a) and (d+a>c):
        sp=(c+a+d)/2
        aria=round(math.sqrt(sp*(sp-c)*(sp-a)*(sp-d)),3)
        perimetru=sp*2
        return print("Laturile",c,',',a,',',d, "pot forma un triunghi, astfel aria acestuia va fi: ",aria,", iar perimetrul: ",perimetru)
(triunghiuri(x,y,z,k))
