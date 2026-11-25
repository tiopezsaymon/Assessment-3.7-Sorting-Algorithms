
# Assessment 3.7: Sorting Algorithms
# Full Name: SAYMON CLINT TIOPEZ
# Sorting Method: Bubble Sort

# Create an array using my full name
name = "SAYMON CLINT TIOPEZ"

# Remove spaces and duplicate letters
unsorted_array = []

for letter in name.upper():
    if letter != " " and letter not in unsorted_array:
        unsorted_array.append(letter)

# Display the unsorted array
print("Unsorted Array:", unsorted_array)

# Bubble Sort Algorithm
sorted_array = unsorted_array.copy()

n = len(sorted_array)

for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_array[j] > sorted_array[j + 1]:
            # Swap letters
            sorted_array[j], sorted_array[j + 1] = sorted_array[j + 1], sorted_array[j]

# Display the sorted array
print("Sorted Array:", sorted_array)
