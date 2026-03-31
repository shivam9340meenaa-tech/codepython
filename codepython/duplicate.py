#find duplicate elements in an array
ar=[1,4,3,1,3,5,7,5,4,2]
duplicate=[]
for i in ar:
    if ar.count(i)>1 and i not in duplicate:
        duplicate.append(i)
print("duplicate:",duplicate)
