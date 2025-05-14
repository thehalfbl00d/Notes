def power(num, powers):
    if powers == 1:
        return num
    return num * power(num, powers - 1)

print(power(2,2))