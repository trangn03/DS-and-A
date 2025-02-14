def insertion_sort(arr):
    # The outer loop iterates over each element in the array starting from the second element.
    for i in range(1, len(arr)):
        # The current element to be compared and inserted into the sorted section of the array.
        current_element = arr[i]

        # The inner loop compares the current element with the elements in the sorted section of the array.
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            # If the current element is smaller, shift the larger elements to the right.
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the current element into its correct position in the sorted section.
        arr[j + 1] = current_element

