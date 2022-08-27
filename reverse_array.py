import numbers


def reverser_array(numbers):
    # [1, 2, 3, 4, 5]
    reversed = []
    #base case
    if len(numbers) == 0:
        return
    
    value = numbers[0]
    reverser_array(numbers[1:])
    
    print(value)
    
def reverse_array_2pointers(numbers, left, right):
    #base case
    if(left >= right):
        return
    
    numbers[right], numbers[left] = numbers[left], numbers[right]
    reverse_array_2pointers(numbers, left + 1, right - 1)
    
def reverse_array_1pointer(numbers, left):
    if left >= len(numbers) / 2:
        return
    
    numbers[len(numbers) - 1 - left], numbers[left] = numbers[left], numbers[len(numbers) - 1 - left]
    reverse_array_1pointer(numbers, left + 1)
    
numbers = [1, 2, 3, 4, 5]
#reverser_array(numbers)
#reverse_array_2pointers(numbers, 0, len(numbers) - 1)
reverse_array_1pointer(numbers, 0)
print(numbers)