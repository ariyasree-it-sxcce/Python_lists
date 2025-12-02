#Count even and odd numbers
#Input: [1, 2, 3, 4, 5, 6] → Output: even=3, odd=3

def even_odd_count(num_list):
    odd_count=0
    even_count=0
    for i in num_list:
        if i%2==0:
            even_count+=1
        else:
            odd_count+=1
    print("Even Count:",even_count)
    print("Odd Count:",odd_count)
even_odd_count([1,2,3,4,5,6]) 

#Time Complexity --> O(n)
#Space Complexity --> O(1)