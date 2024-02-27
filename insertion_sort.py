elements = [54, 23, 87, 98, 2, 101]
n = len(elements)

i=0
j=0

for i in range(1,n):
    key=elements[i]
    j=i-1
    while j>=0 and key<elements[j]:
        elements[j+1]=elements[j]
        j-=1
    elements[j+1]=key

print("Sorted array is:", elements)
