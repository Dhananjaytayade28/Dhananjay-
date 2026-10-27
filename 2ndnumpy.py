import numpy as np

numbers = np.arange(1, 11)
print("Original array:", numbers)

print("First five numbers:", numbers[:5])
print("Numbers from index 2 to 6:", numbers[2:7])
print("Every second number:", numbers[::2])

print("\nArray statistics:")
print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))

updated_numbers = numbers + 10
print("\nAfter adding 10 to each number:", updated_numbers)
