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
'''--------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------'''
#Sum Without Using sum() or '+' Operator
'''
Approach: Can solve by subtraction or bitwise operation
-------------------------------------------------------
XOR → sum without carry

AND + << 1 → carry

Repeat until carry = 0
---------------------------
Solution: 
---------
Step 1: XOR OPERATION

        5 - 101             
        4=  100            
        ----------
            001 ---> 1       
        ----------

Step 2: AND Operation
            101                                   
            110
            ----
            100 <<1 = 1000 = 8 [Left Shift]
                     
Step 3:     1+8=9 

'''

def sum_method(num1,num2):
    while num2 != 0:
        carry = (num1 & num2) << 1 # 8 
        num1 = num1 ^ num2 #num1=1
        num2 = carry  #num2=8
    return num1
print(sum_method(5,4))