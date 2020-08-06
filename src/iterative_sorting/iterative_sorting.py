# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j
             
        # TO-DO: swap
        temp = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = temp

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for _ in range(0, len(arr)-1):
        cur_index = 0
    
        while cur_index < len(arr)-1: 
            # if the previous number is bigger than the next number then swap
            if arr[cur_index] > arr[cur_index+1]:
                
                # Swap
                temp = arr[cur_index]
                arr[cur_index] = arr[cur_index+1]
                arr[cur_index+1] = temp
                
                ## Increment cur_index by 1
                cur_index+=1
            else:
                cur_index+=1

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr