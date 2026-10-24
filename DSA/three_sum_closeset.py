def threeSumClosest(nums, target):
    n = len(nums)
    nums.sort()
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left = i + 1
        right = n - 1
        minDiff = float('inf')
        res_sum = 0
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            diff = abs(s - minDiff)
            if diff < minDiff:
                minDiff = diff
                res_sum = s
            if s == target:
                left = left + 1
                right = right - 1
            if s < target:
                left = left + 1
            else:
                right = right - 1

    return res_sum

nums = [-1, 0, 1, 2, -1, -4]
target = 1
result = threeSumClosest(nums, target)
print(result)