"""
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list

"""

main_list = [i for i in range(1,11)]

extracted_list = main_list[:5]
reversed_list = extracted_list[::-1]

print(extracted_list)
print(reversed_list)