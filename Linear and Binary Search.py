"""
Linear and Binary Search Comparator
CSE1021 - Problem Solving and OOP (Python)
 
Implements linear search and binary search on a list of numbers,
and compares their behaviour (number of comparisons made) on a
sorted dataset.
"""

#Linear Search of a number

user_inp = input("Enter items seperated by spaces:")
my_list = [int(x) for x in user_inp.split()] #Splits the string into a list 
my_list.sort() #Sorts the list in ascending order for binary search
print("List of numbers: ", my_list)

ele = int(input("Enter the no. to search for from the list: "))
linear_comparisons = 0
for i in range(len(my_list)):
    linear_comparisons += 1
    if my_list[i] == ele :
        print("The number was found at actual position :", i+1, "(using Linear Search)")


#Binary Search of a number

def binary_search(my_list, ele):
    low = 0
    high = len(my_list) - 1
    binary_comparisons = 0

    while low <= high:

        binary_comparisons += 1
        middle = (low+high)//2

        if my_list[middle] == ele:
            return middle, binary_comparisons

        elif my_list[middle] > ele:
            high = middle - 1

        else:
            low = middle + 1

    return -1, binary_comparisons


# Run Linear Search
linear_comparisons = 0
linear_pos = -1
for i in range(len(my_list)):
    linear_comparisons += 1
    if my_list[i] == ele:
        linear_pos = i + 1
        break

# Run Binary Search
result_index, binary_comparisons = binary_search(my_list, ele)
print("The number was found at actual position :", result_index + 1, "(using Binary Search)")

binary_pos = result_index + 1 if result_index != -1 else -1

# Print the final comparison report
print("\n--- PERFORMANCE COMPARISON ---")
print(f"Linear Search: {linear_comparisons} comparisons made.")
print(f"Binary Search: {binary_comparisons} comparisons made.")

if linear_comparisons>binary_comparisons :
    print("Binary Search is more effective here due to less no. of comparisons.")





