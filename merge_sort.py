elements = [54, 23, 87, 98, 2, 101]
n = len(elements)
mid = n//2

left = elements[:mid]
right = elements[mid:]
print(range(n),mid, left, right)
i=0
j=0
k=0
elements1=[]

while i <len(left) and j<len(right):
    if left[i] <= right[j]:
        elements[k]=left[i]
        i+=1
    else:
        elements[k]=right[j]
        j+=1
    k+=1

while i<len(left):
    elements[k]=left[i]
    i+=1
    k+=1

while j<len(right):
    elements[k]=right[j]
    j+=1
    k+=1


print("Sorted array is:", elements)
