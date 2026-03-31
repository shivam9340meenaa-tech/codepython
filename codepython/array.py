print("1 Question")
#find the maximum and minimum element in an array
ar=[1,2,3,4,5,6,7,8,9,10]
max=ar[0]
min=ar[0]
for i in ar:
    if i>max:
        max=i
        if i<min:
            min=i
print("max:",max)
print("min:",min)


print("2 Question")
#calculate the sum of elements in an array
ar=[1,2,3,4,5,6,6,7,8,9]
sum=0
for i in ar:
    sum=sum+i
print("sum:",sum)


print("3 Question")
# reverse an array
ar=[2,3,5,6,5,9,8,0]
rev=[0]
for i in ar:
    rev.insert(0,i)
print("reverse:",rev)


print("4 Question")
# find the second largest element in an array
ar=[34,65,78,90,23,54,67]
max=ar[0]
for i in ar:
    if i>max:
        max=i
        second_max=ar[0]
        for i in ar:
            if i>second_max and i!=max:
                second_max=i
print("second largest:",second_max)


print("5 Question")
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


print("6 Question")
#find duplicate elements in an array
ar=[1,4,3,1,3,5,7,5,4,2]
duplicate=[]
for i in ar:
    if ar.count(i)>1 and i not in duplicate:
        duplicate.append(i)
print("duplicate:",duplicate)



print("7 Question")
# move all zeroes to the end of an array
ar=[0,2,1,0,5,8,7,0,6,5,8,4,5]
non_zero=[]
zero=[]
for i in ar:
    if i!=0:
        non_zero.append(i)
    else:
        zero.append(i)
        result=non_zero+zero
print("result:",result)


print("8 Question")
#merge two sortd arrays
ar1=[1,4,3,5,6]
ar2=[2,4,6,1,0]
merged=ar1+ar2
merged.sort()
print("merged:",merged)


print("9 Question")
#find missing numbers in an array(1 to n )
ar=[1,3,5,7,8,9]
n=10
missing=[]
for i in range(1,n+1):
    if i not in ar:
        missing.append(i)
        print("missing:",missing)


print("10 Question")
#find all pairs with a given sum(two sum problem) 
# 
ar=[1,2,3,4,5,6,7,8,9]
target_sum=10
pairs=[]
for i in range(len(ar)):
    for j in range(i+1,len(ar)):
        if ar[i]+ar[j]  == target_sum:
            pairs.append((ar[i],ar[j]))
            print("pairs:",pairs)     