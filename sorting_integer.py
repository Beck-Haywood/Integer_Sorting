def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+k) where n is the num of the numbers and k is the range_int
    Memory usage: O(n) we make an extra array for n numbers"""
    # base case
    if len(numbers) <= 1:
        return numbers
    # Find range of given numbers (minimum and maximum integer values)
    min_int = min(numbers)
    max_int = max(numbers)
    range_int = max_int - min_int + 1
    # Create list of counts with a slot for each number in input range
    array = [0 for i in range(range_int)] 
    # Loop over given numbers and increment each number's count
    for i in numbers:
        array[i - min_int] += 1
    # Loop over counts and append that many numbers into output list
    x=0#define loop count
    y=0
    while x < len(numbers):
        while array[y] < 1:
            y += 1
        # Improve this to mutate input instead of creating new output list
        array[y] -= 1
        numbers[x] = min_int + y
        x += 1

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n^2) is Worst case. Average O(n) 
    Memory usage: O(n) we make an extra array for n numbers"""
    # base case
    if len(numbers) <= 1:
        return numbers
    # Find range of given numbers (minimum and maximum values)
    len_array = len(numbers)
    size = max(numbers) / len_array
    # Create list of buckets to store numbers in subranges of input range
    buckets= []
    for _ in range(len_array):
        buckets.append([]) 
    # Loop over given numbers and place each item in appropriate bucket
    for i in range(len_array):
        index = int (numbers[i] / size)
        if index != len_array:
            buckets[index].append(numbers[i])
        else:
            buckets[len_array - 1].append(numbers[i])
    # Sort each bucket using any sorting algorithm (recursive or another)
    for i in range(len(numbers)):
        insertion_sort(buckets[i])
            
    # Stretch: Improve this to mutate input instead of creating new output list

    index = 0
    for bucket in buckets:
        for i in bucket:
            numbers[index] = i
            index += 1

def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var
array = [5,3]

print(counting_sort(array))
print(array)