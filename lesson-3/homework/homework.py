1. Create and Access List Elements
fruits = ["apple", "banana", "orange", "grape", "mango"]
print(fruits[2])  # Prints the third fruit (index 2)

2. Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)

3. Extract Elements from a List
numbers = [10, 20, 30, 40, 50, 60, 70]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
new_list = [first, middle, last]
print(new_list)

4. Convert List to Tuple
movies = ["Inception", "The Dark Knight", "Interstellar", "The Matrix", "Pulp Fiction"]
movies_tuple = tuple(movies)
print(movies_tuple)

5. Check Element in a List
cities = ["London", "New York", "Tokyo", "Paris", "Berlin"]
print("Paris" in cities)

6. Duplicate a List Without Using Loops
original = [1, 2, 3, 4]
duplicate = original.copy()
print(duplicate)

7. Swap First and Last Elements of a List
numbers = [5, 10, 15, 20, 25]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)

8. Slice a Tuple
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers_tuple[3:8])  # From index 3 to 7 (8 is exclusive)

9. Count Occurrences in a List
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
print(colors.count("blue"))

10. Find the Index of an Element in a Tuple
animals = ("tiger", "lion", "elephant", "giraffe")
print(animals.index("lion"))

11. Merge Two Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)

12. Find the Length of a List and Tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = (10, 20, 30)
print("List length:", len(my_list))
print("Tuple length:", len(my_tuple))

13. Convert Tuple to List
numbers_tuple = (5, 10, 15, 20, 25)
numbers_list = list(numbers_tuple)
print(numbers_list)

14. Find Maximum and Minimum in a Tuple
numbers = (34, 12, 56, 78, 23)
print("Max:", max(numbers))
print("Min:", min(numbers))

15. Reverse a Tuple
words = ("hello", "world", "python", "programming")
reversed_tuple = words[::-1]
print(reversed_tuple)
