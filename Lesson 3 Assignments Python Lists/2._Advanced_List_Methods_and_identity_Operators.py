# Task 1: Given the two lists:
# Find out if Alice submitted their assignment and attended class

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
if "Alice" in submitted and "Alice" in attended:
    print("Alice submitted their assignment and attended class.")
else:
    print("Alice did not submit their assignment or did not attend class.")