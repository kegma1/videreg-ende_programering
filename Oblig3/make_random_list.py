import random

# Generate a list of 10 random integers between 1 and 100
lst = [random.randint(1, 100) for i in range(100_000_000)]

# Write the list to a file called test_list.py
print(lst)