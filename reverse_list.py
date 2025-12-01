# Reverse a list (without using reverse() or slicing)
# Input: [1, 2, 3, 4] → Output: [4, 3, 2, 1]

list_1=[1,2,3,4]
print("List Before Reversing:",list_1)
list_2=[]

for i in range(len(list_1),0,-1):
    list_2.append(i)
print("Reversed List",list_2)