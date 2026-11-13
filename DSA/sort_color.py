def SortColor(nums):
    n = len(nums)
    low = 0
    mid = 0 # point to the current element
    high = n-1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

number = [2, 0, 2, 1, 1, 0]
result = SortColor(number)
print(result)