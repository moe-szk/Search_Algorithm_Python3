# Function : Linear Search
def linear_search(A_arr,a_val):
    for i in range(len(A_arr)):
        if A_arr[i] == a_val:
            return i 
    return -1