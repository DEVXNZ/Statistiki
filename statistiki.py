from tabulate import *
import math
import os
import matplotlib.pyplot as plt

sumN=0
sumF=0
sumF100=0
sumXiNi=0

fi_values=[]
fi100_values=[]
Fi_values=[]
Ni_values=[]
Fi100_values=[]
ai_values=[]


table = []
headers=["xi", "ni", "fi","Ni","Fi","Fi%","fi%","xini","xi**2","xi**2ni","ai"]
synolo_n = 0

os.system('cls' if os.name=='nt' else 'clear')
paratiriseis = int(input("Δωσε πληθος παρατηρησεων: "))


x_values = []
for i in range(paratiriseis):
    x = int(input(f"Δωσε x{i+1}: "))
    x_values.append(x)



n_values = []
for i in range(paratiriseis):
    n = int(input(f"Δωσε ν{i+1}: "))
    synolo_n += n
    n_values.append(n)


for i in range(paratiriseis):
    fi = round(n_values[i] / synolo_n, 2)
    fi_values.append(fi)

    fi100=fi*100
    fi100_values.append(fi100)

    sumN+=n_values[i]
    Ni_values.append(sumN)

    sumF+=fi

    Fi_values.append(sumF)

    sumF100+=fi100

    Fi100_values.append(sumF100)

    xini=x_values[i]*n_values[i]
    sumXiNi+=xini

    xsqr=x_values[i]**2

    xsqrn=(x_values[i]**2)*n_values[i]

    ai=fi*360

    table.append([x_values[i], n_values[i], fi, sumN, sumF, sumF100, fi100, xini, xsqr, xsqrn,ai])

os.system('cls' if os.name=='nt' else 'clear')
print(tabulate(table, headers),"\n")

x_meso=round(sumXiNi/synolo_n, 2)
print(f'Το x μεσο ειναι: {x_meso}')

def diakimansi(x_meso):
    sum=0
    for i in range(paratiriseis):
        ssqr=((x_values[i]-x_meso)**2)*n_values[i]
        sum+=ssqr
        calculation=sum/synolo_n
    return calculation


apotelesma_diakimansis=round(diakimansi(x_meso), 2)
print(f'Η διακυμανση s**2 ειναι: {apotelesma_diakimansis}')

s=round(math.sqrt(apotelesma_diakimansis), 2)
print(f"Το αποτελεσμα της τυπικης αποκλησης ειναι: {s}")

CV=round(s/abs(x_meso), 2)*100.0
print(f"το CV ειναι: {CV} %")

if CV <= 10/100.0:
    print("Το δειγμα παρουσιαζει ομοιογενια")
else:
    print("Το δειγμα δεν παρουσιαζει ομοιογενια")


def istograma(x, y, y_label):
    plt.bar(x, y)
    plt.xlabel("xi")
    plt.ylabel(y_label)
    return plt.show()

question=input("θελουμε γραφιμα?: ")
while question !="":
    grafima=input("δωσε γραφιμα: ")
    if grafima=="ni":
        istograma(x_values, n_values, "ni")
    elif grafima=="fi":
        istograma(x_values, fi_values, "fi")
    elif grafima=="fi%":
        istograma(x_values, fi100_values, "fi%")
    elif grafima=="Ni":
        istograma(x_values, Ni_values, "Ni")
    elif grafima=="Fi":
        istograma(x_values, Fi_values, "Fi")
    else:
        istograma(x_values, Fi100_values, "Fi%") 
    question=input("θελουμε γραφιμα?: ")



    
    

















    