# Generate cubes number pattern from 1 to 10
# 1 8 27 64 ...

START = 1
END = 10
power = 3

for i in range(START, END+1):
    print(i**power)
