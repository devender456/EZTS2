def bubble_sort(my_list):
    n = len(my_list)

    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

# Example usage:
my_list = [64, 34, ,1,  2]
bubble_sort(my_list)

print("Sorted array:", my_list)
