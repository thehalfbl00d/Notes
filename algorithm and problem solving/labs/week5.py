# 3 some problem
# this a brute force algorithm
def main():
    array = [ 30, -30 , 0, 1, -1 , 20, -20, 10, 10, 100]
    count = 0
    it = 0
    for i in range(len(array) - 2):
        for j in range(i+ 1, len(array) -1):
            for x in range(j + 1, len(array)):
                it +=1
                if array[i] + array[j] + array[x] == 0:
                    print(f"({array[i]})+({array[j]})+({array[x]}) = 0")
                    count+=1
    print(it)
    return count

print(main())

