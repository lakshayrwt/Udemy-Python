pangram = "The quick brown fox jumps over the lazy dog"

words = pangram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

generated_lists = [
    '9','',
    '2','2','3','',
    '3','7','2','',
    '0','3','6','',
    '8','5','4','',
    '7','7','5','',
    '8','0','7','']
values = "".join(generated_lists)
print(values)

values_list = values.split()
print(values_list)

#mini challenge
#1
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])

print(values_list)

#2
integer_values = []
for value in values_list:
    integer_values.append(int(values))

print(integer_values)