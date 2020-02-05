# What is the time complexity of this sort?
 
# List contains positive integers (can include 0).
my_list = [6, 4, 12, 63, 11, 25, 11, 29, 5, 46, 32, 34, 7]

# Find largest and smallest in list to define range.
smallest = my_list[0]
largest = my_list[0]
for element in my_list:
    if element > largest:
        largest = element
    elif element < smallest:
        smallest = element

# Make new list to track which numbers appear.
track_list = [0] * (largest - smallest + 1)

# Add 1 to index of element's value - smallest.
for element in my_list:
    track_list[element - smallest] += 1

# Print tracked list.
for i, ii in enumerate(track_list):
    print(ii + smallest, i)

# Init sorted list.
sorted_list = []

# Recreate my_list in sorted order.
for i, value in enumerate(track_list):
    # Skip zeros.
    if value == 0:
        continue
    
    # For non-zeros, add the index to the sorted list 'value' times.
    for _ in range(value):
        sorted_list.append(i + smallest)

# Print sorted list.
print(sorted_list)
