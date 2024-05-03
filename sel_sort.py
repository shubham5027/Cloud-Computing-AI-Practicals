def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Taking input from the user
arr = []
n = int(input("Enter the number of elements in the array: "))
print("Enter the elements of the array:")
for i in range(n):
    element = int(input())
    arr.append(element)

# Sorting the array using selection sort
selection_sort(arr)

# Printing the sorted array
print("Sorted array:", arr)
