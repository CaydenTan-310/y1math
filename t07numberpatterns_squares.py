# Generate squares number pattern from 1 to 10
# 1 4 9 16 25 ...

START = 1
END = 10
power = 2

for i in range(START, END+1):
    print(i**power)
