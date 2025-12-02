def sum_of_elements(list_1):
    print("Sum(using function):",sum(list_1))    #using sum() function

    #Sum of elements in a list by looping
    add=0
    for i in list_1:
        add+=i
    print("Sum(using iteration):",add)
sum_of_elements([1,2,3,4])

#Time Complexity --> O(n)
#Space Complexity --> O(1)