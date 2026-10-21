def remove_duplicate(nums):
    n = len(nums)

    if n == 0:
        return 0

    left = 0
    right = 1
    unique = 1

    while right < n:
        if nums[right] == nums[right - 1]:
            right += 1
        else:
            nums[left + 1] = nums[right]
            left += 1
            right += 1
            unique += 1

    return unique


nums = [1, 1, 2, 2, 3, 4, 4, 5]

result = remove_duplicate(nums)

print(result)