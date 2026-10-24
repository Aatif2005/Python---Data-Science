def threeSum(nums):
    n = len(nums)
    nums.sort()
    ans = []

    for i in range(n - 2):

        if nums[i] > 0:
            break

        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        sum_ = -nums[i]

        while left < right:

            s = nums[left] + nums[right]

            if s == sum_:
                ans.append([nums[i], nums[left], nums[right]])

                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif s > sum_:
                right -= 1

            else:
                left += 1

    return ans


nums = [-1, 0, 1, 2, -1, -4]
result = threeSum(nums)
print(result)