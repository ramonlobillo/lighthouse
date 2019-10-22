########################
# Binary search
########################
# Aim: Find the position of a specific value in an ordered list of values.
# Input: list of sorted integers. Value to find.
# Output: position of desired value in the input array.
# * Complexity: 
# How many times can you divide N by 2 until you have 1?
# --> log2 (n)
#  
# You can divide log N times until you have everything divided. 
# Which means you have to divide log N ("do the binary search step") 
# until you found your element.

def binary_search(arr, initial_pos, final_pos, findme): 

    # Check base case 
    if final_pos >= initial_pos: 

        mid = int(initial_pos + (final_pos - initial_pos)/2)

        # If element is present at the middle itself 
        if arr[mid] == findme: 
            return mid 
        
        # If element is smaller than mid, then it 
        # can only be present in left subarray 
        elif arr[mid] > findme: 
            return binary_search(arr, initial_pos, mid-1, findme) 

        # Else the element can only be present 
        # in right subarray 
        else: 
            return binary_search(arr, mid + 1, final_pos, findme) 

    else: 
        # Element is not present in the array 
        return -1
    
# END binary_search

def main():
    
    # Input values. input_array must be sorted.
    inputarray = [2, 3, 4, 10, 40, 50, 125, 300] 
    findme = 50
    
     
    result = binary_search(inputarray, 0, len(inputarray)-1, findme) 
    if result != -1: 
        print("Element is present at index % d" % result) 
    else: 
        print("Element is not present in array")

#END main

if __name__ == '__main__':
    main()
