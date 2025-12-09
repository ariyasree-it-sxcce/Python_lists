#Find the maximum and minimum value
#Input: [10, 3, 6, 2] → Output: max=10, min=2

def max_and_min(list):
    print("Maximum of List:",max(list))
    print("Minimum of list:",min(list))
max_and_min([10, 3, 6, 2])
max_and_min([-10,-3,-6,-2])

#Time Complexity --> O(n)
#Space Complexity --> O(1)
'''-----------------------------------------------------------------------------------------------'''
#Find max & min WITHOUT using max(), min() but using sorting

def maxMinBySort(lst):
    lst.sort()
    print("\nMinimum Element:",lst[0])
    print("Maximum Element:",lst[-1])
maxMinBySort([10,-2,15,100])

'''-----------------------------------------------------------------------------------------------'''
#Find the max & min difference (range)

def rangeOfList(lst):
    print("\nRange of List:",max(lst)-min(lst))
rangeOfList([10, 3, 6, 2])

'''-----------------------------------------------------------------------------------------------'''

#Return INDEX of max & min, not values

# Using loop
def max_and_min(lst):
    max=lst[0]
    min=lst[0]
    max_index=0
    min_index=0
    for i in range(0,len(lst)):
        if lst[i]>max:
            max=lst[i]
            max_index=i
        if lst[i]<min:
            min=lst[i]
            min_index=i
    print("Index of Max Element:",max_index)
    print("Index of Min Element:",min_index)
max_and_min([10, 3, 6, 21])
#------------------------------------------------------------
#Using min(),max() and index() functions 
def indexValue(lst):
    print("Index of Max(using function):",lst.index(max(lst)))
    print("Index of Min(Using function):",lst.index(min(lst)))
indexValue([10, 3, 6, 20])

'''-----------------------------------------------------------------------------------------------'''
def rangeOfList(lst):
    print("\nRange of List:",max(lst)-min(lst))
rangeOfList([10, 3, 6, 2])

'''-----------------------------------------------------------------------------------------------'''
#Find max & min WITHOUT using max(), min(), or sorting

def maxAndmin(lst):
    max=0
    min=0
    for i in range(0,len(lst)):
        if lst[i]>max:
            max=lst[i]
            min=max
        if lst[i]<min:
            min=lst[i]
    print("\nMaximum Element=",max)
    print("Minimum Element:",min)
maxAndmin([10,55,2,33])
maxAndmin([-11,5,-1])  # max=5 and min=-1 but min=-11 hence break logic 

#Above code fails in list of negative numbers
#So corrected Code

def maxAndmin2(lst):
    max=lst[0]
    min=lst[0]
    for i in range(0,len(lst)):
        if lst[i]>max:
            max=lst[i]
        if lst[i]<min:
            min=lst[i]
    print("\nMaximum Element=",max)
    print("Minimum Element:",min)
maxAndmin2([10,-55,2,33])
maxAndmin2([-10,-55,-2,-33])

