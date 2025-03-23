nums = [12,3,4,5,6,7,8,9,10,11]

n = len(nums)
for i in range(n):
    for j in range(i+1,n):
        min = i
        if nums[j] < nums[i]:
            min = j
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp
        print(nums)

