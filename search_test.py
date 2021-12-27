from linear_search import linear_search

import numpy as np
from time import process_time


# Input the number of data.
print("Input the number of data.")
n = input()

# Generate array of random numbers 
# and index for search values
A_arr = np.random.randint(int(n)*100,size=int(n))
index_arr = np.random.randint(int(n),size=10)

index = 0

# Search
m = int(1)
while int(m) != 0:
    print("1:Linear Search \
    \n0:Quit")
    
    m = input()

    test_flag = True
    t1 = process_time()
    for i in range(10):
        if int(m)==1:
            index = linear_search(A_arr,A_arr[index_arr[i]])
        
        # Check
        if index_arr[i] != index and m!=0:
            test_flag = False
    t2 = process_time()

    # Check and output
    if test_flag:
        print('Search succeeded.')
    elif int(m)!=0:
        print("** Search failed.**")
    print("Time : ",(t2-t1)/10)