def duplicate(lst):
    # Dictionary to count occurrences of each number
    count = {}
    
    # List to store duplicates
    duplicates = []
    
    # Count occurrences of each number in the list
    for number in lst:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    
    # Find numbers that occur more than once
    for number, freq in count.items():
        if freq > 1:
            duplicates.append(number)
    
    return duplicates

# Example usage
numbers = [1, 3, 5, 7, 3, 9, 1, 2, 5, 8]
print("Duplicates in the list:", duplicate(numbers))
