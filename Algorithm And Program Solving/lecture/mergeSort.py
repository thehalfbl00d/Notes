array = [10, 11, 2,5,3,4,1,5,3,2,9,2, 10, 22]

def mergeSort(A):

    if len(A) < 2:
        return A
    
    mid = len(A) // 2

    left = A[:mid]
    right = A[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    merged = merge(left,right)

    return merged


def merge(left, right):
    temp = []
    i  = j =  0
    while i < len(right) and j < len(left):
        if right[i] < left[j]:
            temp.append(right[i])
            i+=1
        else:
            temp.append(left[j])
            j+=1

    temp.extend(left[j:]) # need to understand these
    temp.extend(right[i:]) # need to understand this too
    return temp

        

print(mergeSort(array))


