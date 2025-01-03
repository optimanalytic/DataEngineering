def mean(numbers):
    """Returns the mean of a list of numbers."""
    return sum(numbers) / len(numbers)


def median(numbers):
    """Returns the median of a list of numbers."""
    numbers.sort()
    if len(numbers) % 2 == 0:
        mid1 = numbers[len(numbers) // 2]
        mid2 = numbers[len(numbers) // 2 - 1]
        return (mid1 + mid2) / 2
    else:
        return numbers[len(numbers) // 2]
