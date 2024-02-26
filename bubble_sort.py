elements = [54, 23, 87, 98, 2, 101]
n = len(elements)
print(range(n))
for i in range(n):
    for j in range(0, n-i-1):
        if elements[j]>elements[j+1]:
            elements[j], elements[j+1] = elements[j+1], elements[j]

print("Sorted array is:", elements)
