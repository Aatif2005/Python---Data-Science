def segregate0and1(numbers):
    n = len(numbers)
    left = 0
    right = n-1
    while left < right:
        if numbers[left] == 0:
            left +=1
        elif numbers[right] == 1:
            right -=1
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left +=1
            right -=1
    return numbers
numbers = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
result = segregate0and1(numbers)
print(result)