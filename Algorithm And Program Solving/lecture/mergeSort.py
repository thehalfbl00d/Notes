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

    # we are adding these incase there is left on any side, these arrays wont be non-empty at the same time, only one of them will have data in it
    temp.extend(left[j:]) 
    temp.extend(right[i:]) 

    return temp
'''
the merge function is like a situation where there is a bus with one entrance.
and there are two lines of people
the condition is, the person nearest to the door on both lines have to filtered based on the height
the smallest person is allowed each time.

there might be condition where wheither some of them is left in one line but it's not possible that there are left on both lines
Dont worry about the left overs on each side, they are already sorted :)
'''

        

print(mergeSort(array))


