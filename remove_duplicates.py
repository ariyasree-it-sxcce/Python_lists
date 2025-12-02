#Remove duplicates (without using set)
#Input: [1,2,2,3,4,4,5] → Output: [1,2,3,4,5]


def duplicate_free(list_1,list_2):
    for i in list_1:
        if i not in list_2:
            list_2.append(i)
    print("Duplicate free list:",list_2)
duplicate_free([1,2,2,3,4,4,5],[])

#Time Complexity --> O(n^2)
#Space Complexity --> O(n)