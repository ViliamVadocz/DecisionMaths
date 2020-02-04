# What is the time complexity of this sort?

# List contains positive integers (can include 0).
my_list = [6,4,12,63,11,0,25,11,29,5,46,1]

# Find largest in list.
largest = my_list[0]
for element in my_list:
    if element > largest:
        largest = element

# Make new list of length 'largest + 1'.
track_list = [0] * (largest + 1)

# Add 1 to index of element's value.
for element in my_list:
    track_list[element] += 1

# Init sorted list.
sorted_list = []

# Recreate my_list in sorted order.
for i, value in enumerate(track_list):
    # Skip zeros.
    if value == 0:
        continue
    
    # For non-zeros, add the index to the sorted list 'value' times.
    for _ in range(value):
        sorted_list.append(i)

# Print sorted list.
print(sorted_list)
