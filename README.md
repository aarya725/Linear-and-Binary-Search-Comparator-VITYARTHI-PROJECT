# Linear and Binary Search Comparator

A Python program that runs Linear Search and Binary Search on the same dataset, counts how many comparisons each algorithm makes to find a target element, and reports which one performed better.

## Overview

Searching is one of the most fundamental operations in computer science, and the algorithm you choose can make a big difference in performance. This project demonstrates that difference empirically rather than just theoretically, by actually counting comparisons instead of only stating Big-O complexity.

The program:
1. Takes a list of numbers and a target element (ele) to search for.
2. Runs Linear Search, counting every comparison made.
3. Runs Binary Search, counting every comparison made.
4. Prints the position at which the element was found by each method.
5. Compares the number of comparisons made by both algorithms and declares which was more efficient for that run.

## How It Works

### Linear Search
- Iterates through the list from index 0 to len(my_list) - 1.
- Increments a comparison counter (linear_comparisons) on every check.
- Stops as soon as a match is found (break) and records the 1-indexed position.
- If no match is found, position remains -1.

```python
linear_pos = -1
for i in range(len(my_list)):
    linear_comparisons += 1
    if my_list[i] == ele:
        linear_pos = i + 1
        break
```

### Binary Search
- Requires the list to be sorted.
- Repeatedly divides the search interval in half, comparing the middle element to the target.
- Returns the index of the match along with the total number of comparisons made (binary_comparisons).

```python
result_index, binary_comparisons = binary_search(my_list, ele)
binary_pos = result_index + 1 if result_index != -1 else -1
```

### Performance Report
After both searches run, the program prints a summary and determines the winner:

```python
print("\n--- PERFORMANCE COMPARISON ---")
print(f"Linear Search: {linear_comparisons} comparisons made.")
print(f"Binary Search: {binary_comparisons} comparisons made.")

if linear_comparisons > binary_comparisons:
    print("Binary Search is more effective here due to less no. of comparisons.")
```

## Sample Output

```
The number was found at actual position : 7 (using Binary Search)

--- PERFORMANCE COMPARISON ---
Linear Search: 7 comparisons made.
Binary Search: 3 comparisons made.
Binary Search is more effective here due to less no. of comparisons.
```

(Exact numbers depend on the list size and the position of the target element.)

## Time Complexity

| Algorithm      | Best Case | Average Case | Worst Case | Requires Sorted Data? |
|----------------|-----------|---------------|------------|------------------------|
| Linear Search  | O(1)      | O(n)          | O(n)       | No                     |
| Binary Search  | O(1)      | O(log n)      | O(log n)   | Yes                    |

Binary Search is generally faster for large, sorted datasets, but Linear Search does not require the data to be sorted beforehand, which is its main practical advantage.

## Getting Started

### Prerequisites
- Python 3.x installed on your system

### Running the Project
```bash
git clone https://github.com/aarya725/Linear-and-Binary-Search-Comparator-VITYARTHI-PROJECT.git
cd Linear-and-Binary-Search-Comparator-VITYARTHI-PROJECT
python3 "Linear and Binary Search.py"
```

You can modify my_list and ele inside the script to test different datasets and target values.

## What This Project Demonstrates
- Practical, hands-on understanding of two core searching algorithms
- The ability to instrument code to measure real algorithmic performance, not just theoretical complexity
- Comparative analysis and conditional reporting based on runtime metrics

## Future Improvements
- Accept list and target as user input (or command-line arguments) instead of hardcoding them
- Add support for multiple test cases in a single run
- Visualize comparison counts across different list sizes using matplotlib
- Add unit tests to verify correctness for edge cases (empty list, duplicate elements, element not present)

## Author
Vaibhavi Aarya

## License
This project is open source and available for educational use.
