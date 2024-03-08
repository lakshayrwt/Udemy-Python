empty = []
even = [2 , 4 , 6 , 8]
odd = [1 , 3 , 5 , 7 , 9]
# print(min(even))
# print(max(even))
# print()
# print(min(odd))
# print(max(odd))
# print()
# print(len(even))
# print(len(odd))

# print("yomoyomoyoyo".count("yo"))

# even.append(10)
# print(max(even))

# even.extend(odd)
# print(even)
# even.sort()
# print(even)
# even.sort(reverse=True)
# print(even)
numbers = even + odd
sorted_numbers = sorted(numbers)

digits = sorted("8534916720")
print(digits)

# more_numbers = list(numbers)
# more_numbers = numbers[:]
more_numbers = numbers.copy()
print(more_numbers)
print(more_numbers is numbers)
print(more_numbers == numbers)