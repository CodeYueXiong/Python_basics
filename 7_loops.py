# normal
z = [7, 5, 9, 3, 8]
for number in z:
    print(number)
# enumerate
friends = ['steve', 'rachel', 'ross', 'monika', 'chandler', 'joey']
for friend in enumerate(friends):
    print(friend)
# break and continue
# task: introduce the range function
odd_numbers = []
even_numbers = []
for number in range(1, 51):
    if number % 2 == 0:
        even_numbers.append(number)
    elif number % 2 !=0:
        odd_numbers.append(number)

print(f"odd numbers are {odd_numbers}")
print(f"even numbers are {even_numbers}")