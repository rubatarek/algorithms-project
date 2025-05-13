# Function to perform insertion sort
def insertion_sort(a): 

    n = len(a)   # Get the length of the array "a"

    # Iterate over the array starting from index 1 to end
    for j in range (1,len(a)):   

        key = a[j]   # Element to insert
        i = j - 1   # Shift the elements sorted to the right to make space for the key

        while i >= 0 and a[i] > key :   
          a[i+1] = a[i] 
          i = i - 1
          a[i +1] = key   # Insert the key at the correct position

    return a

# Example
a = [3,9,7,6,13,34]     
print("Input", a)
sorted_array = insertion_sort(a)
print("Output", sorted_array)

# Function to perform merge sort
def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    
    merged = []
    left_index = right_index = 0

    # Merge while comparing the smallest elements
    while left_index < len(left) and right_index < len(right):

        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add elements of the array
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

# Function to perform quick sort
def quick_sort(arr):

    if len(arr) <= 1:
        return arr  # Base case: already sorted
    
    pivot = arr[0]  # Choose the first element as the pivot
    less = [x for x in arr[1:] if x <= pivot]  # Elements less than or equal to pivot
    greater = [x for x in arr[1:] if x > pivot]  # Elements greater than pivot

    return quick_sort(less) + [pivot] + quick_sort(greater)

# Example 
print("Sorted")
a = [1, 3, 5, 6, 7, 8, 9, 45 ,67,89]
print("Input array:", a)
sorted_array = quick_sort(a)
print("Output array:",sorted_array)
