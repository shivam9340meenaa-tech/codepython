# count the number of even and odd elements in an array
ar=[1,2,4,6,5,9,0,11,13,7]
even=0
odd=0
for i in ar:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("even:",even)
print("odd:",odd)