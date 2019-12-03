a = [0] * 10
b = [[],[],[],[],[],[],[],[],[],[]]

for i in range(1000):

    total = 0
    for digit in str(i):
        total += int(digit)

    if total < 10: 
        a[total] += 1
        b[total].append(i)

print(a)
for i, row in enumerate(b):
    print(i, row)
