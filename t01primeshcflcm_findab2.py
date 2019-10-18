# If a and b are integers such that a * b = 18, find the possible values of a + b.

multiplication = 18

factors = []
factors2 = []
e=0
for i in range(1, multiplication+1):
    if multiplication % i == 0:
        e+=1
e=e/2
for i in range(1, multiplication+1):
    if multiplication % i == 0:
        if (i <= e):
            factors.append(i)
        else:
            factors2.append(i)

e=0
while e!=len(factors):
    print(factors[e]+factors2[0-(e+1)])
    e+=1
