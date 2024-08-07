def group(lst, size):
    # List to hold the result of grouped lists
    grouped_list = []
    
    # Iterate through the list in steps of the given size
    for i in range(0, len(lst), size):
        # Slice the list from i to i+size and add it to grouped_list
        grouped_list.append(lst[i:i + size])
    
    return grouped_list

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
group_size = 3
print("Grouped list:", group(my_list, group_size))
