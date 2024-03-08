pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram)
print(letters)

numbers = [2.5 , 8.1 , 3.9 , 4.8 , 5.5 , 6.2 , 7.3]
another_numbers = sorted(numbers)
print(numbers)
print(another_numbers)

numbers.sort()
print(numbers)

missing_words = sorted("the quick brown fox jumped over the lazy dog", 
                       key=str.casefold)
print(missing_words)

names = ["Kuroko",
         "kise",
         "Aomine",
         "midorima",
         "Murakibara",
         "Akashi"]
names.sort(key=str.casefold)
print(names)