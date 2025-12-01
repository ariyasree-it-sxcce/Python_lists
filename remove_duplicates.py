#Remove duplicates (without using set)
#Input: [1,2,2,3,4,4,5] → Output: [1,2,3,4,5]

list_1=[1,2,2,3,4,4,5]
list_2=[]
for i in list_1:
    if i not in list_2:
        list_2.append(i)
print("Duplicate free list:",list_2)