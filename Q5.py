def lensort(strings):
    return sorted(strings, key=len)

# Example usage
string_list = ["apple", "banana", "kiwi", "grapes", "cherry"]
print("Sorted by length:", lensort(string_list))
def extsort(files):
    """
    Sorts a list of file names based on their file extension.
    
    :param files: List of file names to be sorted
    :return: List of file names sorted by extension
    """
    return sorted(files, key=lambda x: x.split('.')[-1] if '.' in x else '')

# Example usage
file_list = ["document.txt", "image.png", "archive.zip", "data.csv", "presentation.ppt"]
print("Sorted by extension:", extsort(file_list))
