# bounce.py
#
# Exercise 1.5

current_height = 100
divisor = 3/5

for i in range(10):
    current_height = current_height * divisor
    print(round(current_height, 4))