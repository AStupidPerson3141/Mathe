from random import randint
from time import time
open("ans.txt", "w").write("")
open("data.txt", "w").write("")
start = time()
for i in range(1000):
    print("generating randoms")
    a = randint(-100, 150)
    b = randint(-5, 10)
    print(f"generated {a} and {b}")
    print('opening and writing to file "data.txt')
    open("data.txt", "a").write(f"{a}_{a+b}\n")
    print('opening and writing to file "ans.txt"')
    open("ans.txt", "a").write(f"{a+2*b}\n")
end = time()
print(f"finished at time {end-start}")