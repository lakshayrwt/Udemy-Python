even = [2 , 4 , 6 , 8]
odd = [1 , 3 , 5 , 7 , 9]
print(min(even))
print(max(even))
print()
print(min(odd))
print(max(odd))
print()
print(len(even))
print(len(odd))

print("yomoyomoyoyo".count("yo"))

even.append(10)
print(max(even))

even.extend(odd)
print(even)
even.sort()
print(even)
even.sort(reverse=True)
print(even)