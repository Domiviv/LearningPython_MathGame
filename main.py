import random

MIN = 1
MAX = 10
N = 3


def sub():
    flag = False
    a = random.randint(MIN, MAX)
    b = random.randint(MIN, MAX)
    result = a - b
    while not flag:
        s = input(f"{a} - {b} = ")
        try:
            c = int(s)
            if c == result:
                print(f"Nice one!")
                flag = True
            else:
                print(f"Wrong Answer")
                return False
        except ValueError:
            print(f"ERROR: {s} is not a number. Please try again.")
    return flag


def add():
    flag = False
    a = random.randint(MIN, MAX)
    b = random.randint(MIN, MAX)
    result = a + b
    while not flag:
        s = input(f"{a} + {b} = ")
        try:
            c = int(s)
            if c == result:
                print(f"Nice one!")
                flag = True
            else:
                print(f"Wrong Answer")
                return False
        except ValueError:
            print(f"ERROR: {s} is not a number. Please try again.")
    return flag


def mul():
    flag = False
    a = random.randint(MIN, MAX)
    b = random.randint(MIN, MAX)
    result = a * b
    while not flag:
        s = input(f"{a} * {b} = ")
        try:
            c = int(s)
            if c == result:
                print(f"Nice one!")
                flag = True
            else:
                print(f"Wrong Answer")
                return False
        except ValueError:
            print(f"ERROR: {s} is not a number. Please try again.")
    return flag


def div():
    flag = False
    a = random.randint(MIN, MAX)
    b = random.randint(MIN, MAX)
    result = a / b
    while not flag:
        s = input(f"{a} / {b} = ")
        try:
            c = float(s)
            if c == result:
                print(f"Nice one!")
                flag = True
            else:
                print(f"Wrong Answer")
                return False
        except ValueError:
            print(f"ERROR: {s} is not a number. Please try again.")
    return flag


def avg(n):
    nb = int(n / 2)
    return nb


score = 0
for i in range(0, N):
    print(f"\nQuestion {i+1}/{N}")
    o = random.randint(0, 3)
    if o == 0:
        res = add()
    elif o == 1:
        res = sub()
    elif o == 2:
        res = div()
    elif o == 3:
        res = mul()

    if res:
        score += 1

print(f"\nHere's your score : {score}/{N}")
average = avg(N)
if score == N:
    print("\nPerfect!")
elif score == 0:
    print("\nReally bad!")
elif score > average:
    print("\nWell...")
else:
    print("\nNot really good...")

